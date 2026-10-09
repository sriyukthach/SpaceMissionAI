from groq import Groq

from config import GROQ_API_KEY, GROQ_MODEL
from backend.prompts import SYSTEM_PROMPT
from backend.vector_store import search_documents


def get_chatbot_response(question):

    if not GROQ_API_KEY or GROQ_API_KEY.startswith("your_"):
        return "Please configure your Groq API key in .env.", []

    relevant_docs = search_documents(question)

    if not relevant_docs:
        return "No knowledge documents found.", []

    context = "\n\n".join(
        f"Source: {doc['source']}\n{doc['text']}"
        for doc in relevant_docs
    )

    user_prompt = f"""
    Reference Documents:
    {context}

    Student Question:
    {question}

    Explain the answer in simple educational language.

    Use the reference documents.
    If the documents do not contain enough information,
    explain that the information is unavailable.
    """

    try:
        client = Groq(api_key=GROQ_API_KEY)

        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.3,
            max_completion_tokens=700
        )

        answer = response.choices[0].message.content

        sources = list(dict.fromkeys(
            doc["source"] for doc in relevant_docs
        ))

        return answer or "No response generated.", sources

    except Exception as error:
        print(
            f"Groq API error: "
            f"{type(error).__name__}: {error}"
        )

        return (
            "Groq could not generate a response. "
            "Check the VS Code terminal for the error.",
            []
        )