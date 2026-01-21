from app.rag.index import model, index, docs
import numpy as np


def retrieve(query, k=2):
    q_emb = model.encode([query])
    _, idx = index.search(np.array(q_emb), k)
    return [docs[i] for i in idx[0]]
