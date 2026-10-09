from groq import Groq

from config import GROQ_API_KEY, GROQ_MODEL
from backend.prompts import SYSTEM_PROMPT
from backend.vector_store import search_documents

REFUSAL_MESSAGE = (
    "Sorry, this question is outside my knowledge base. "
    "I can only answer questions based on the provided "
    "space mission documents."
)

def get_chatbot_response(question):

    # Check API key
    if not GROQ_API_KEY or GROQ_API_KEY.startswith("your_"):
        return "Please configure your Groq API key in .env.", []

    # Retrieve relevant documents from ChromaDB
    relevant_docs = search_documents(question)

    if not relevant_docs:
        return REFUSAL_MESSAGE, []

    # Build context using retrieved document chunks
    context = "\n\n".join(
        f"Source: {doc['source']}\nContent: {doc['text']}"
        for doc in relevant_docs
    )

    try:
        client = Groq(api_key=GROQ_API_KEY)

        # STEP 1: Validate whether the documents support the answer
        validation = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a document-based question validator. "
                        "Your job is to determine whether the supplied "
                        "reference documents contain enough information "
                        "to answer the user's question. "
                        "Respond with exactly one word: YES or NO. "
                        "Return YES when the documents contain information "
                        "that directly answers the question or clearly "
                        "supports a simple explanation. "
                        "Return NO when the question is unrelated or "
                        "the documents lack the necessary information. "
                        "Do not use outside knowledge. "
                        "Do not provide explanations."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"REFERENCE DOCUMENTS:\n{context}\n\n"
                        f"QUESTION:\n{question}\n\n"
                        "Can the question be answered using these documents? "
                        "Reply YES or NO."
                    ),
                },
            ],
            temperature=0,
            max_completion_tokens=512,
        )

        # Read validation response
        choice = validation.choices[0]
        raw_decision = choice.message.content or ""
        decision = raw_decision.strip().upper()

        # Debugging information in VS Code terminal
        print("\n========== RAG VALIDATION ==========")
        print("QUESTION:", question)
        print("VALIDATION RESPONSE:", repr(raw_decision))
        print("VALIDATION DECISION:", repr(decision))
        print("FINISH REASON:", choice.finish_reason)
        print("====================================\n")

        # Reject questions not supported by the documents
        if decision != "YES":
            return REFUSAL_MESSAGE, []

        # STEP 2: Generate answer from the documents
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": (
                        f"REFERENCE DOCUMENTS:\n{context}\n\n"
                        f"USER QUESTION:\n{question}\n\n"
                        "Explain the answer clearly in simple language. "
                        "Use ONLY information supported by the documents. "
                        "Do not add outside knowledge. "
                        "If the documents do not support the answer, "
                        f"respond exactly: {REFUSAL_MESSAGE}"
                    ),
                },
            ],
            temperature=0.2,
            max_completion_tokens=1024,
        )

        answer = (response.choices[0].message.content or "").strip()

        if not answer:
            return REFUSAL_MESSAGE, []

        # Show sources only for successfully answered questions
        sources = list(
            dict.fromkeys(
                doc["source"] for doc in relevant_docs
            )
        )

        if answer == REFUSAL_MESSAGE:
            return answer, []

        return answer, sources

    except Exception as error:
        print(
            f"Groq API error: "
            f"{type(error).__name__}: {error}"
        )

        return (
            "Unable to generate a response. "
            "Check the VS Code terminal for details.",
            [],
        )