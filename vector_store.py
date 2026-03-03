import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()
class VectorStore:
    def __init__(self):
        self.model=SentenceTransformer('all-MiniLM-L6-v2')
        self.index_path="vector_index.faiss"
        self.index=None
        self.text_chunks=[]
    def create_index(self,chunks):
        self.text_chunks=chunks
        embeddings=self.model.encode(chunks)
        dimension=embeddings.shape[1]
        self.index=faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings))
        faiss.write_index(self.index, self.index_path)
        print(f"Index saved to {self.index_path}")
    def load_index(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
            print("Index loaded from disk.")
            return True
        return False
    def search(self,query,k=3):
        query_embedding=self.model.encode([query])
        distances,indices=self.index.search(np.array(query_embedding),k)
        return [self.text_chunks[i] for i in indices[0]]
        
        
        