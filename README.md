# 🚀 SpaceMissionAI
### Space Mission Operations & Launch Process Explainer Bot

**An AI-powered educational chatbot making space mission knowledge simple, interactive, and accessible.**

🌐 **Live Application:** https://spacemissionai.streamlit.app/

## 📌 About the Project

SpaceMissionAI is a Generative AI-powered educational chatbot designed to explain complex space mission operations, rocket launch processes, satellite deployment, and mission control activities in simple, understandable language.

The project uses **Retrieval-Augmented Generation (RAG)** and **Google Gemini Flash** to provide AI-generated explanations supported by relevant educational documents.

Developed as part of a **2-Day Generative AI Workshop**, this project demonstrates the practical application of Large Language Models (LLMs), document processing, embeddings, vector databases, and responsible AI in the aerospace domain.

## 🎯 Problem Statement

Space missions involve complex preparation, launch sequences, mission planning, and mission control processes. Technical aerospace documentation is often difficult for students, beginners, and the general public to understand.

SpaceMissionAI addresses this challenge by providing an intelligent, interactive chatbot that simplifies aerospace concepts through natural language explanations.

## ✨ Key Features

- 🤖 **AI-Powered Chatbot:** Interactive question-answering using Google Gemini Flash.
- 🚀 **Space Mission Explanations:** Understand rocket launches, satellite deployment, and mission control.
- 📚 **Retrieval-Augmented Generation:** Retrieves relevant information from educational documents.
- 🧩 **Document Chunking:** Divides large documents into smaller, manageable sections.
- 🔍 **Semantic Search:** Uses vector embeddings to identify relevant content.
- 🗄️ **Vector Database:** ChromaDB stores and retrieves document embeddings.
- 💬 **Streamlit Interface:** Simple, interactive, and beginner-friendly web application.
- 🔒 **Responsible AI:** Restricted to educational explanations without spacecraft control or operational simulations.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Streamlit | Web application interface |
| Google Gemini Flash | Generative AI model |
| Google AI Studio API | LLM integration |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database |
| PyPDF | PDF document processing |
| LangChain Text Splitters | Document chunking |
| Git & GitHub | Version control |
| Streamlit Community Cloud | Application deployment |

## 🏗️ System Architecture

The application follows a Retrieval-Augmented Generation (RAG) workflow.

**Document Processing:**

`Space Mission Documents → Text Extraction → Text Chunking → Embedding Generation → ChromaDB`

**Question Answering:**

`User Question → Streamlit Interface → Semantic Search → Relevant Document Retrieval → Gemini Flash → AI-Generated Explanation`

### How It Works

1. Educational space mission documents are loaded into the system.
2. Documents are divided into smaller text chunks.
3. Each chunk is converted into a numerical vector embedding.
4. Embeddings are stored in the ChromaDB vector database.
5. The user submits a question through the Streamlit interface.
6. The system retrieves the most relevant document chunks.
7. Gemini Flash processes the retrieved context and generates an educational explanation.
8. The answer is displayed through the chatbot interface.

## 💬 Example Questions

Users can ask questions such as:

- Explain the rocket launch sequence.
- What happens during mission control?
- Explain the satellite deployment process.
- What is pre-launch testing?
- What are the stages of mission planning?
- How do satellites reach their intended orbit?
- What is the role of ground control stations?

## 🌐 Live Demo

**Try SpaceMissionAI here:**

🚀 https://spacemissionai.streamlit.app/

The application is deployed using **Streamlit Community Cloud**, allowing users to explore space mission concepts directly through their web browsers.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.11 or 3.12
- Internet connection
- Google Gemini API key

### Step 1: Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd SpaceMissionAI
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key

Create a `.env` file in the project directory and add:

```env
GEMINI_API_KEY=your_api_key_here
```

Obtain an API key from Google AI Studio:

https://aistudio.google.com/api-keys

**Important:** Never upload your actual API key or `.env` file to GitHub.

### Step 4: Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

`http://localhost:8501`

## 🔒 Responsible AI and Safety

SpaceMissionAI is designed exclusively for educational and informational purposes.

The application does not:

- Control spacecraft or launch systems.
- Execute real-world mission commands.
- Perform operational mission simulations.
- Access live spacecraft telemetry.
- Replace professional aerospace mission systems.

Its purpose is to make space science and mission operations easier to understand.

## 🎓 Learning Outcomes

Through this project, we explored:

- Generative AI and Large Language Models.
- Retrieval-Augmented Generation (RAG).
- Document processing and text chunking.
- Vector embeddings and semantic similarity search.
- ChromaDB vector database integration.
- Gemini API integration.
- Streamlit web application development.
- Cloud deployment and responsible AI practices.

## 👥 Project Information

**Project Number:** 44

**Project Title:** Space Mission Operations & Launch Process Explainer Bot

**Industry Domain:** Space & Aerospace Operations

**Workshop:** 2-Day Generative AI Workshop

**Application:** SpaceMissionAI

**Deployment:** Streamlit Community Cloud

## 📌 Project Status

🚀 **Deployed**

🌐 **Live Application:** https://spacemissionai.streamlit.app/

---

### ⭐ SpaceMissionAI — Exploring Space Through Artificial Intelligence

*Making complex aerospace knowledge accessible, understandable, and interactive for everyone.*
