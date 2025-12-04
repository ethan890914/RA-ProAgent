from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict
import json
from query_loader import query_loader
class ProAgentRAG:
    def __init__(self, history, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.embeddings = []
        self.history = history

    def load_history(self, history):
        query = history['task']
        additions = history['additional_information']

        # todo: handle workflow node if necessary
        # workflow = history['workflow']
        # function_call = history['function_call']
        # llm_io = history['llm_io']

        record = ""
        record += f"query: {query}"
        record += f"additional information: {additions}"
        return record

    def build_index(self,):
        texts = [self.load_history(item) for item in self.history]
        self.embeddings = self.model.encode(texts)

    def retrieve_similar(self, query, top_k=3):
        query_embedding = self.model.encode([query])[0]

        # Cosine similarity
        similarities = np.dot(self.embeddings, query_embedding) / (
                np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )

        top_indices = np.argsort(similarities)[-top_k:][::-1]

        results = []
        for idx in top_indices:
            results.append({
                'id': self.history[idx]['ID'],
                'similarity': float(similarities[idx]),
                'query': self.history[idx]['task']
            })

        return results


### Sample usage
if __name__ == '__main__':
    query_file = "queries_data.json"

    with open(query_file) as f:
        query_library = json.load(f)

    query = '''
    Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each news headline as 'technology' or 'sport', and sends results to Slack. Each Slack message contains a single news-category pair.
    '''
    rag = ProAgentRAG(query_library)
    rag.build_index()
    res = rag.retrieve_similar(query)

    print(res)