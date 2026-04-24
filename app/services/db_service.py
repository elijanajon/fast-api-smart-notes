import os

from azure.cosmos import CosmosClient

COSMOS_URL = os.getenv("COSMOS_URL")
COSMOS_KEY = os.getenv("COSMOS_KEY")

client = CosmosClient(COSMOS_URL, COSMOS_KEY)

database = client.get_database_client("notes-db")
container = database.get_container_client("notes")