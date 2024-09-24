from wilhelm_python_sdk.ancient_greek_neo4j_loader import load_into_database

if __name__ == "__main__":
    cleanup_neo4j()
    load_into_database("ancient-greek.yaml")
