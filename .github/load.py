from wilhelm_python_sdk.database_manager import cleanup_neo4j
from wilhelm_python_sdk.german_neo4j_loader import load_into_database

if __name__ == "__main__":
    cleanup_neo4j()
    load_into_database("german.yaml")
