from setuptools import find_packages
from setuptools import setup

setup(
    name="graph-database-loader",
    version="0.0.1",
    description="A package suitable for offline vocabulary processing and batch ingestion into Graph databases, " +
                "such as Neo4j and ArangoDB",
    url="https://github.com/QubitPi/Antiqua/tree/master/graph-database-loader",
    author="Jiaqi Liu",
    author_email="jack20220723@gmail.com",
    license="Apache-2.0",
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=["neo4j", "python-arango", "pyyaml", "datasets"],
    zip_safe=False,
    include_package_data=True,
    setup_requires=["setuptools-pep8", "isort"],
    test_suite='tests',
)
