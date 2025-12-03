import os
import json
from typing import Dict, Any

class Credentials():
    def __init__(self, base_file_path="./ProAgent/n8n_tester/credentials"):
        """
        Initializes the object with the given base file path. If no base file path is provided,
        the default path "./ProAgent/n8n_tester/credentials" will be used.

        Parameters:
            base_file_path (str): The base file path to the credentials directory. Defaults to
                                  "./ProAgent/n8n_tester/credentials".

        Return:
            None
        """
        with open(os.path.join(base_file_path, "c.json"), "r", encoding="utf-8") as reader:
            credential_data = json.load(reader)
            self.credential_data: Dict[str, Any] = {}
            for item in credential_data:
                item_info = {
                    "name": item["name"],
                    "id": item["id"],
                    "type": item["type"],
                }

                # Handle credentials with or without nodesAccess field
                if "nodesAccess" in item and item["nodesAccess"]:
                    # Use the provided nodesAccess if available
                    for node_type in item["nodesAccess"]:
                        node_type_name = node_type["nodeType"].split(".")[-1]
                        if self.credential_data.get(node_type_name, -1) == -1:
                            self.credential_data[node_type_name] = []
                        self.credential_data[node_type_name].append(item_info)
                else:
                    if self.credential_data.get(item["type"], -1) == -1:
                        self.credential_data[item["type"]] = []
                    self.credential_data[item["type"]].append(item_info)

                    # Map credential types to actual node types from your workflow
                    type_mapping = {
                        "openAiApi": [
                            "lmChatOpenAi",  # From @n8n/n8n-nodes-langchain.lmChatOpenAi
                            "OpenAi",
                            "openAi",
                            "ChatOpenAi",
                            "aiCompletion"
                        ],
                        "serpApi": [
                            "toolSerpApi",  # From @n8n/n8n-nodes-langchain.toolSerpApi
                            "SerpApi",
                            "serpApi"
                        ],
                        "googleSheetsOAuth2Api": ["googleSheets"],
                        "slackApi": [
                            "slack",  # Standard Slack node
                            "Slack",
                            "slackTrigger",  # Slack Trigger node
                            "SlackTrigger"
                        ],
                        "slackOAuth2Api": [
                            "slack",  # Standard Slack node with OAuth2
                            "Slack",
                            "slackTrigger",  # Slack Trigger node with OAuth2
                            "SlackTrigger"
                        ],
                        "gmailOAuth2": [
                            "gmail",
                            "Gmail",
                            "gmailTrigger",
                            "GmailTrigger",
                            "Gmail account"
                        ],
                        "googleDriveOAuth2Api": ["googleDrive"],
                        "httpHeaderAuth": [
                            "httpRequest",  # HTTP Request node
                            "HttpRequest",
                            "newsapi"  # Alias for NewsAPI usage
                        ],
                        "openWeatherMapApi": [
                            "openWeatherMap",  # Standard OpenWeatherMap node
                            "OpenWeatherMap"
                        ]
                        # Add more mappings as needed
                    }

                    # Get possible node type names for this credential type
                    possible_node_types = type_mapping.get(item["type"], [item["type"]])

                    # Add the credential info for all possible node types
                    for node_type_name in possible_node_types:
                        if self.credential_data.get(node_type_name, -1) == -1:
                            self.credential_data[node_type_name] = []
                        self.credential_data[node_type_name].append(item_info)

        # Load workflow data
        try:
            with open(os.path.join(base_file_path, "w.json"), "r", encoding="utf-8") as reader:
                workflow_data = json.load(reader)
                if workflow_data and len(workflow_data) > 0:
                    self.workflow_id = workflow_data[0]["id"]
                else:
                    self.workflow_id = "mock-workflow-id"
        except FileNotFoundError:
            print("Warning: w.json not found, using mock workflow ID")
            self.workflow_id = "mock-workflow-id"
                
    def get_workflow_id(self) -> str:
        """
        Get the workflow ID.
        :return: The workflow ID.
        :rtype: str
        """
        return self.workflow_id

    def query(self, node_type):
        """
        Retrieves the last element of the credential data associated with the given node type.

        Parameters:
            node_type (str): The type of node.

        Returns:
            The last element of the credential data associated with the given node type, or None if the node type is not found.
        """
        if self.credential_data.get(node_type,-1) == -1:
            print(f"Warning: No credentials found for node type '{node_type}'")
            print(f"Available node types: {list(self.credential_data.keys())}")
            return None
        return self.credential_data[node_type][-1]

    def list_available_credentials(self):
        """
        List all available credential types for debugging.
        """
        print("Available credentials:")
        for node_type, creds in self.credential_data.items():
            for cred in creds:
                print(f"  {node_type}: {cred['name']} (ID: {cred['id']}, Type: {cred['type']})")
 
credentials = Credentials()
