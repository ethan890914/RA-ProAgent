import os

from sentence_transformers import SentenceTransformer
import numpy as np
import json

def include_all_info(query, additions=None):
    return f'''query: {query}
    additional information: {additions}
    '''
class ProAgentRAG:
    def __init__(self, query_file="queries_data.json", model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.embeddings = []
        self.history = {}
        self.index_data = None

        with open(query_file) as f:
            history = json.load(f)

        self.build_disjoint_sets(history)
        self.build_index()

    def build_disjoint_sets(self, history):
        for record in history:
            ## optional: use baseflow only
            res = {
                "task": record["task"],
                "additional_information": record["additional_information"],
            }
            ancestor_file = os.path.join("apa_case_storage", f"ID_{record['ID']}", "ancestor.json")
            if not os.path.exists(ancestor_file):
                res["parent"] = record["ID"]
            else:
                with open(ancestor_file, "r") as f:
                    data = json.load(f)
                    res["parent"] = data["base_workflow_id"]
            self.history[record["ID"]] = res

    def find_src(self, id, record):
        while record["parent"] != id:
            id = record["parent"]
            record = self.history[id]
        return id

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
            src = self.find_src(self.index_data['keys'][idx], self.history[self.index_data['keys'][idx]])
            if src in srcs:
                continue
            srcs.append(src)
            if float(similarities[idx]) < threshold: break
            results.append({
                'key': self.index_data['keys'][idx],  # Direct indexing
                # 'text': self.index_data['texts'][idx],
                'similarity': float(similarities[idx])
            })
            if len(results) == top_k:
                break
        return srcs

### Sample usage
if __name__ == '__main__':

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

    rag = ProAgentRAG()
    res = rag.retrieve_similar(query)

    print(res)