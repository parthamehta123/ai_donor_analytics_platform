from app.rag.retrieval import retrieve


def answer(query: str):
    context = "\n".join(retrieve(query))
    prompt = f"""
Use only the context below.
If answer is missing, say "I don't know".

Context:
{context}

Question: {query}
"""
    return prompt
