=====================
Graph Database Loader
=====================

.. contents:: Table of Contents
    :depth: 2


Being a standalone subproject of Antiqua, `Graph Data Loader <https://pypi.org/project/graph-database-loader/>`_ is a
bundle of data pipeline that reads Antiqua's vocabulary from supported data sources and loads them into graph databases

Some features of it can be reused as SDK. This documentation walks through how to use the SDK

Install
=======

To install the SDK, simply run::

    pip install graph-database-loader

Neo4J Database Client
=====================

1. Make ready a Neo4J database instance. A free one can be obtained at https://console.neo4j.io
2. Set the following environment variables

   - **NEO4J_URI**: the connection URL of the database, such as "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
   - **NEO4J_DATABASE**: the database name
   - **NEO4J_USERNAME**: the username for connecting the database
   - **NEO4J_PASSWORD**: the user's password for the connection

  where all of them are available when database is provisioned on https://console.neo4j.io

3. Load data into Neo4J database:

   .. code-block:: python


      from database.neo4j.database_clients import get_database_client

      with get_database_client() as database_client:
          database_client.save_a_node_with_attributes("MyNoteType1", {"label": "My Node 1"})
          database_client.save_a_node_with_attributes("MyNoteType2", {"label": "My Node 2"})

          database_client.save_a_link_with_attributes(
                language="English",
                source_label="My Node 1",
                target_label="My Node 2",
                attributes={"label": "My Link"}
            )


If we would like to empty database, we can do

.. code-block:: python

   from database.neo4j.database_manager import cleanup_neo4j

   if __name__ == "__main__":
       cleanup_neo4j()

Note that this function targets the same database with the same credentials listed above

API Documentation
=================

.. automodule:: database.neo4j.database_clients
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: database.neo4j.database_manager
   :members:
   :undoc-members:
   :show-inheritance:

Development
===========

Create virtual environment and install dependencies::

    git clone git@github.com:QubitPi/Antiqua.git
    cd Antiqua/graph-database-loader
    python3 -m venv .venv
    . .venv/bin/activate

Then generate egg information from the `setup.py` and use the requirements.txt from these egg information to install all
the dependencies for development::

    python setup.py egg_info
    pip install -r graph-database-loader.egg-info/requires.txt
