# 📚 Week 3 – Retrieval-Augmented Generation (RAG)

This week focuses on implementing a complete Retrieval-Augmented Generation (RAG) system using LlamaIndex and OpenAI. The goal was to enhance LLM responses by grounding them in real-world documents through vector search and chunk-based retrieval.

---

## ✅ Objectives

- ✅ Implement document **chunking** and **embedding**
- ✅ Build a vector-based **retriever**
- ✅ Use a response **synthesizer** to generate grounded, citation-style answers
- ✅ Compare RAG results vs. prompt-only queries
- ✅ Understand how chunking impacts retrieval quality

---

## 🛠️ Tools & Technologies

- **LlamaIndex v0.12.35**
- **OpenAI API (gpt-3.5-turbo + text-embedding-3-small)**
- Python, Jupyter Notebook
- PDF/Text document loader
- `SentenceSplitter` for chunking
- `CompactAndRefine` synthesizer for answers

---

## 🧠 What I Built

- A custom RAG pipeline that:
  - Loads a real document from a `data/` folder
  - Splits it into overlapping chunks (512 tokens, 100 overlap)
  - Embeds those chunks into a vector index using OpenAI embeddings
  - Allows natural language queries via a retriever and synthesizer
  - Returns an answer with supporting evidence from the document

---