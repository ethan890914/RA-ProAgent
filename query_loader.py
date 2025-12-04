import json
import os
from ProAgent.utils import userQuery


class query_loader():
    """
    Query loader class that loads all query definitions from queries_data.json

    Queries are stored in a dictionary with ID as key.
    Use get_single_query(ID) to retrieve a specific query.
    """

    def __init__(self, queries_file='queries_data.json'):
        self.queries = {}
        self.queries_file = queries_file
        self.load_queries()

    def load_queries(self):
        """
        Load all queries from queries_data.json
        Each query in the JSON file contains: ID, task, additional_information, refine_prompt
        """
        # Get the directory where this file is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, self.queries_file)

        # Load JSON file
        with open(json_path, 'r', encoding='utf-8') as f:
            queries_data = json.load(f)

        # Convert each JSON object to userQuery
        for query_dict in queries_data:
            query = userQuery(
                ID=query_dict['ID'],
                task=query_dict['task'],
                additional_information=query_dict['additional_information'],
                refine_prompt=query_dict.get('refine_prompt', '')
            )
            self.load_single_query(query)

    def load_single_query(self, userQuery):
        """
        Load a single query into the queries dictionary
        If ID already exists, it will be overwritten with a warning
        """
        if userQuery.ID in self.queries:
            # overwrite the old query
            print(f'userQuery.ID = {userQuery.ID} is duplicated, the old query was overwritten!')
        self.queries[userQuery.ID] = userQuery

    def get_single_query(self, ID):
        """
        Retrieve a query by ID
        Returns the query if found, otherwise raises an error
        """
        if ID in self.queries and self.queries[ID] is not None:
            return self.queries[ID]
        else:
            print(f'Query with ID={ID} not existed!')
            assert False, f"Query ID={ID} not found"
            return self.queries.get('default')

    def load_workflow_from_storage(self, old_ID, storage_dir='apa_case_storage'):
        """
        Load workflow data from apa_case_storage/ID_X directory

        Loads the final successful workflow code from tool_call_logs directory.

        Args:
            old_ID: The ID of the old workflow to load
            storage_dir: The base directory for storage (default: 'apa_case_storage')

        Returns:
            dict with 'query' (userQuery object) and 'workflow_code' (str: final workflow code)
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        workflow_dir = os.path.join(current_dir, storage_dir, f'ID_{old_ID}')

        if not os.path.exists(workflow_dir):
            raise FileNotFoundError(f"Workflow directory not found: {workflow_dir}")

        # Load the query from queries_data.json
        old_query = self.get_single_query(old_ID)

        # Load the final workflow code from tool_call_logs
        tool_call_logs_dir = os.path.join(workflow_dir, 'tool_call_logs')
        workflow_code = None

        if os.path.exists(tool_call_logs_dir):
            # Get all Python files and sort them
            code_files = sorted([f for f in os.listdir(tool_call_logs_dir) if f.endswith('_code.py')])

            if code_files:
                # Get the last (final) workflow code file
                final_code_file = code_files[-1]
                with open(os.path.join(tool_call_logs_dir, final_code_file), 'r', encoding='utf-8') as f:
                    workflow_code = f.read()

        if workflow_code is None:
            raise FileNotFoundError(f"No workflow code found in {tool_call_logs_dir}")

        return {
            'query': old_query,
            'workflow_code': workflow_code
        }
