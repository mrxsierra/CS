---
title: LLMs & AI Orchestration
tags: ['stack/data']
created: 2026-06-10
---

# LLMs & AI Orchestration

## Overview
LLMs dominate 2026 interviews — every role from ML Engineer to Product Manager needs to understand how to build AI-powered applications. Focus on RAG architectures, agent patterns, and prompt engineering.

## The RAG Architecture (Retrieval-Augmented Generation)

### Why RAG?
LLMs have a knowledge cutoff and can hallucinate. RAG grounds LLM responses in actual data:
```
User Query → Retrieve relevant docs → Augment prompt → Generate grounded response
```

### RAG Pipeline Components
```python
# 1. Document Ingestion
from langchain_community.document_loaders import PDFLoader, WebLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

docs = PDFLoader("document.pdf").load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 2. Embedding & Vector Store
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone, Chroma

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_documents(chunks, embeddings)

# 3. Retrieval + Generation
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o"),
    retriever=vectorstore.as_retriever(search_k=5),
    return_source_documents=True,
)
response = qa_chain.invoke("What is the revenue for Q3?")
```

### Advanced RAG
- **Hybrid Search**: Vector similarity + keyword (BM25) → best of both
- **Query Rewriting**: LLM rewrites "Tell me about Q3" → "Q3 2025 revenue and metrics"
- **Multi-Hop RAG**: Break complex questions into sub-questions, retrieve for each
- **Self-RAG**: LLM evaluates if retrieved docs are relevant before generating

## Agent Patterns

### ReAct (Reasoning + Acting)
```python
agent = create_react_agent(
    llm=ChatOpenAI(model="gpt-4o"),
    tools=[search_tool, calculator_tool, database_tool],
    prompt="You are a data analyst. Answer questions by searching, computing, and querying."
)

# Agent loop: Think → Act → Observe → Repeat
# Think: "I need to find Q3 revenue from the sales database"
# Act: query_database("SELECT SUM(revenue) FROM sales WHERE quarter = 'Q3'")
# Observe: "$4.2M"
# Answer: "Q3 revenue was $4.2 million."
```

### Tool Calling
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                },
                "required": ["location"],
            },
        },
    }
]
```

## Prompt Engineering Patterns

| Pattern | Technique | Use Case |
|---------|-----------|----------|
| **Zero-shot** | "Classify this email as spam or not-spam" | Simple tasks |
| **Few-shot** | Provide 2-3 examples in the prompt | Complex classification |
| **Chain-of-Thought** | "Let's think step by step" | Math, logic, reasoning |
| **Tree-of-Thoughts** | Explore multiple reasoning paths | Creative problem-solving |
| **System Prompt** | "You are a helpful coding assistant" | Role definition |
| **Structured Output** | "Return JSON with fields: name, age" | Data extraction |

## LLM Evaluation

### Metrics
- **ROUGE**: N-gram overlap with reference → summarization
- **BLEU**: Precision of n-grams → translation
- **BERTScore**: Semantic similarity using BERT embeddings
- **LLM-as-Judge**: Use GPT-4 to rate output quality
- **RAGAS**: RAG-specific metrics (faithfulness, relevance, context precision)

### Hallucination Detection
```python
# Check if the LLM response is grounded in retrieved context
def check_hallucination(response, context_chunks):
    prompt = f"""Determine if the following answer is supported by the context.
    Context: {context_chunks}
    Answer: {response}
    Is the answer fully supported by the context? Reply YES or NO."""
    result = llm.invoke(prompt)
    return "NO" in result  # Hallucinated!
```

## Common Interview Questions

1. **"Explain the RAG architecture."** — Retrieve relevant documents from a vector store, inject them into the LLM prompt alongside the user query, so the LLM generates a response grounded in your data.

2. **"How do you handle hallucination?"** — RAG (ground in real data), self-reflection (ask LLM to verify), confidence thresholds, human-in-the-loop for critical decisions.

3. **"What is the difference between fine-tuning and RAG?"** — Fine-tuning updates model weights for a specific task (expensive, rigid). RAG adds external context at inference time (cheap, flexible, always up-to-date).

4. **"How do you choose chunk size for RAG?"** — Smaller chunks (~200-300 tokens) for focused retrieval. Larger chunks (~1000 tokens) for more context. Overlap of 10-20% to avoid cutting off important info.

## Related Topics
- [[08_stack_deep_dives/03_data_ai_stack/04_deep_learning|Deep Learning Foundations]]
- [[08_stack_deep_dives/03_data_ai_stack/06_mlflow_deployment|MLOps & Model Deployment]]
- [[08_stack_deep_dives/03_data_ai_stack/index|Data & AI Stack Index]]
- [[02_role_tracks/04_ml_engineer|ML Engineer Track]]

## Resources
- [LangChain Docs](https://python.langchain.com/docs)
- [OpenAI Platform Docs](https://platform.openai.com/docs)
- [Building LLM Apps (Chip Huyen)](https://huyenchip.com/2024/07/02/llm-apps.html)