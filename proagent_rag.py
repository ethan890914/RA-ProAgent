from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Dict
import json
from query_loader import query_loader
def include_all_info(query, additions=None):
    record = ""
    record += f"query: {query}"
    record += f"additional information: {additions}"
    return record
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

        return include_all_info(query, additions)

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
                'ID': self.history[idx]['ID'],
                'similarity': float(similarities[idx]),
                'query': self.history[idx]['task']
            })

        return results


### Sample usage
if __name__ == '__main__':
    query_file = "queries_data.json"

    with open(query_file) as f:
        query_library = json.load(f)

    # task = '''
    # Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each news headline as 'technology' or 'sport', and sends results to Slack. Each Slack message contains a single news-category pair.
    # '''

    task = '''
    Whenever I trigger the Manual Trigger, execute the workflow, which reads data from googleSheets, uses aiCompletion to classify each commercial entry Description as 'to Business' or 'to Customer', and emails the result or send it to slack.'''

    additions = [
      "1.1 The documentId(\"mode\": \"id\") of Google Sheet is: 1JiMU318fRZguk7LmfvpeDKg72vv34bfeSjTdwl0Sj7c",
      "1.2 The sheetName of Google is: commercial",
      "1.3 The sheet has one title row with value \"Business Line\", \"Manager\", \"cost\", \"sales\", \"Description\" and has several commercial entries below.",
      "2.1 For each commercial entry from Google Sheets, create an aiCompletion input with messages array containing system prompt and user prompt",
      "2.2 System prompt: 'You are a news classifier. Classify as 'to Business' or 'to Customer'.'",
      "2.3 User prompt: Include the actual commercial entry's Description text",
      "2.4 aiCompletion should process each of the commercial entry separately",
      "3.1 Parse aiCompletion output to extract the category ('to Business' or 'to Customer')",
      "3.2 If it's a 'to Business' commercial entry, then send it through slack.",
      "3.3 If it's a 'to Customer' commercial entry, then send it through email.",
      "4.1 slack format:",
      "4.2 Send results to slack channel #general",
      "4.3 Each slack message format: 'Commercial Entry: [Description]\nCategory: [category]'",
      "5.1 email format:",
      "5.2 Send results with Gmail to qwuqwuqwu@gmail.com",
      "5.3 Each email abstract: Commercial Entry: [Description]",
      "5.4 Each email content format: 'Commercial Entry: [Description]\nCategory: [category]'"
    ]
    query = include_all_info(task, additions)

    rag = ProAgentRAG(query_library)
    rag.build_index()
    res = rag.retrieve_similar(query)

    print(res)