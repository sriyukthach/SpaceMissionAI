# 🚀 SpaceMissionAI
### Space Mission Operations & Launch Process Explainer Bot

## 📌 About the Project

SpaceMissionAI is a Generative AI-powered chatbot designed to simplify complex space mission operations and launch processes for students, beginners, and space enthusiasts.

The application uses **Retrieval-Augmented Generation (RAG)** and Google's **Gemini Flash** model to provide clear, educational explanations based on space mission documents.

## 🎯 Problem Statement

Space missions involve complex planning, launch preparation, satellite deployment, and mission control operations. Technical documentation can be difficult for beginners to understand.

SpaceMissionAI addresses this challenge by providing an interactive AI chatbot that explains aerospace concepts in simple, accessible language.

## ✨ Features

- Interactive chatbot using Streamlit.
- AI-powered explanations using Gemini Flash.
- Document-based question answering using RAG.
- Text chunking and vector embeddings.
- Semantic search using ChromaDB.
- Educational explanations of launch and mission operations.
- Responsible AI restrictions to prevent operational spacecraft control.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Streamlit | Web interface |
| Google Gemini API | AI-generated explanations |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database |
| PyPDF | PDF text extraction |
| LangChain Text Splitters | Document chunking |

## ⚙️ System Workflow

1. Space mission documents are loaded into the system.
2. Documents are divided into smaller text chunks.
3. Text chunks are converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. Users submit questions through the Streamlit interface.
6. Relevant document chunks are retrieved using similarity search.
7. Gemini generates an educational explanation using the retrieved information.

## 💬 Sample Questions

- Explain the rocket launch sequence.
- What happens during mission control?
- Explain the satellite deployment process.
- What is pre-launch testing?
- What are the stages of space mission planning?

## 🚀 How to Run

**Step 1: Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
cd SpaceMissionAI
```

**Step 2: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 3: Configure Gemini API**

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_api_key_here
```

**Step 4: Start the application**

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal.

## 🔒 Responsible AI

SpaceMissionAI is strictly an educational application. It does not control spacecraft, execute mission commands, simulate real missions, or access live mission control systems.

## 👥 Team

Developed as part of a **Generative AI Workshop**.

**Industry Domain:** Space & Aerospace Operations

**Project:** 44 – Space Mission Operations & Launch Process Explainer Bot

## 📌 Project Status

🚧 Under Development

---

⭐ **SpaceMissionAI — Exploring Space Through Artificial Intelligence.**
