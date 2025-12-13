import json

import numpy as np
from sentence_transformers import SentenceTransformer


def include_all_info(query, additions=None):
    return f'''query: {query}
    additional information: {additions}
    '''
class ProAgentRAG:
    def __init__(self, query_file="./task_library/base_flow.json", model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.embeddings = []
        self.history = {}
        self.index_data = None

        with open(query_file) as f:
            history = json.load(f)

        self.format_record(history)
        self.build_index()

    def format_record(self, history):
        for record in history:
            res = {
                "task": record["task"],
                "additional_information": record["additional_information"],
            }
            self.history[record["ID"]] = res


    def build_index(self,):
        keys = list(self.history.keys())
        texts = [include_all_info(self.history[key]["task"], self.history[key]["additional_information"]) for key in keys]
        embeddings = self.model.encode(texts)

        # Store keys alongside embeddings
        self.index_data = {
            'keys': keys,  # Store as array
            'embeddings': embeddings,
            'texts': texts
        }

    def retrieve_similar(self, query, top_k=3, threshold=0.8):
        query_embedding = self.model.encode([query])[0]

        similarities = np.dot(self.index_data['embeddings'], query_embedding) / (
                np.linalg.norm(self.index_data['embeddings'], axis=1) *
                np.linalg.norm(query_embedding)
        )

        top_indices = np.argsort(similarities)[:][::-1]
        results = []
        srcs = []
        for idx in top_indices:
            srcs.append(self.index_data['keys'][idx])
            if float(similarities[idx]) < threshold: break
            results.append({
                'key': self.index_data['keys'][idx],  # Direct indexing
                'similarity': float(similarities[idx])
            })
            if len(results) == top_k:
                break
        return srcs

if __name__ == '__main__':

    query = "send the financial news to my gmail"

    rag = ProAgentRAG()
    res = rag.retrieve_similar(query)
    print(res)