<h1 align="center">
   Classes Information Retrieval System
</h1>

<div align="center">  
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />  
  <img src="https://img.shields.io/badge/NLTK-FF4500?style=for-the-badge&logo=nltk&logoColor=white" />  
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />  
  <img src="https://img.shields.io/badge/NLP-006B6B?style=for-the-badge&logo=natural-language-processing&logoColor=white" />  
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />  
  <img src="https://img.shields.io/badge/Poetry-4E227A?style=for-the-badge&logo=poetry&logoColor=white" />  
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" />  
</div>

---

**Information Retrieval System** is a Python-powered information-retrieval engine that lets you index entire document collections, interpret free-form queries, and return relevance-ranked answers—all with no external service required.

Unlike a simple CSV search that scans each row for literal query matches, IR model builds a TF-IDF vector index and applies NLP preprocessing (tokenization, lemmatization, stop-word removal) so that queries and documents are compared in a high-dimensional space using cosine similarity—yielding fast, relevance-ranked results rather than unranked, exact‐match hits, and allowing seamless extension to more advanced ranking algorithms like BM25 or neural embeddings.

## Table of Contents

- [Features](#features)
- [Application](#application)
- [Installation](#installation)

## Features

- **Local Indexing**: Builds a TF-IDF vector index over your document collection (any pandas DataFrame column) on initialization—no external services involved.  
- **Custom NLP Pipeline**: Leverages `query_processing()` for tokenization, normalization, stop-word removal and lemmatization to turn free-form queries into polished search inputs.  
- **Fast Similarity Search**: Transforms queries into TF-IDF vectors and computes cosine similarity against your corpus to generate relevance scores in milliseconds.  
- **Top-N Ranking**: Returns a configurable number of results, sorted by descending score, including document ID, metadata fields (e.g. Major, Course Title), cleaned description, and relevance score.  
- **Persistence & Reuse**: Keeps the fitted `TfidfVectorizer` and index in memory or disk (your choice) so subsequent searches are instant and consistent across runs.  
- **Schema-Agnostic**: Simply point the system at any DataFrame and column name—no fixed schema required, making it easy to index PDFs, CSVs or custom data sources.  
- **Extensible Scoring**: Core TF-IDF + cosine similarity can be augmented with additional ranking algorithms (BM25, neural embeddings) as your needs evolve.  

## Application

![ScreenShot - 12AM-48M@2x](https://github.com/user-attachments/assets/1496d230-0226-4807-bb54-127721c04d10)

## Installation

### Prerequisites

- **Docker**

### Steps

1. **Clone the repository**:

```bash
git clone https://github.com/vladimircuriel/information-retrieval-system
```

2. **Navigate to the project directory**:

```bash
cd information-retrieval-system
```
   
3. **Run the commands**:

```bash
docker build -t system:latest .
```

```bash
docker run -p 8501:8501 system:latest
```
4. **Access the application**:

Open your browser and visit `http://localhost:8501` to access the user interface.

