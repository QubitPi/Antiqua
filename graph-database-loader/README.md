Wilhelm Data Loader
===================

![Python Version][Python Version Badge]
[![Read the Docs][Read the Docs badge]][Read the Docs URL]
[![PyPI][PyPI project badge]][PyPI project url]
[![GitHub Workflow Status][GitHub Workflow Status badge]][GitHub Workflow Status URL]
[![Apache License badge]][Apache License URL]

Wilhelm Data Loader is a bundle of data pipeline that reads [wilhelmlang.com]'s vocabulary from supported data sources
and loads them into graph databases

Some features can be reused as SDK which can be installed via

```console
pip install wilhelm_data_loader
```

Details documentations can be found at [sdk.wilhelmlang.com](https://sdk.wilhelmlang.com/)

Wiktionary Data Loader (Arango DB)
----------------------------------

[graph-database-loader]() works naturally for single-tenant application, the [wilhelmlang.com]. In order to support
cross-language inferencing, all data are hence loaded into a __single__
[Database](https://arango.qubitpi.org/stable/concepts/data-structure/#databases). Data of each langauge resides in
dedicated [Collections](https://arango.qubitpi.org/stable/concepts/data-structure/#collections)

There are _n + 2_ Collections loaded:

- _n_ document collections for n languages supported by [wiktionary-data](https://github.com/QubitPi/wiktionary-data)
- _1_ document collection for "Definition" entity, where the English definition of each word resides in one
  [document](https://arango.qubitpi.org/stable/concepts/data-structure/#documents)
- _1_ edge collection for connections between words and definitions as well as those among words themselves

> [!TIP]
>
> See [_Collection Types_](https://arango.qubitpi.org/stable/concepts/data-structure/collections/#collection-types) for
> differences between document & edge collections

Each collection generates index on the word term. If the term comes with a gender modifier, such as
"das Audo" (_car_, in German), a new
[computed attribute](https://arango.qubitpi.org/stable/concepts/data-structure/documents/computed-values/) that has
the modifier stripped-off is used for indexing instead

Wilhelm Vocabulary Loader
-------------------------

> [!CAUTION]
>
> When the graph database is Neo4J, all constrains relating to the __Term__ node must be using:
>
> ```cypher
> SHOW CONSTRAINTS
> DROP CONSTRAINT constraint_name;
> ```
>
> This is because certain vocabulary has multiple grammatical forms. This vocabulary is spread out as multiple entries.
> These multiple entries, because they have lots of common properties, often triggers constraint violations in Neo4J on
> load

The absolute fastest way (by far) to load large datasets into neo4j is to use the bulk loader

The cache here is defined as the set of all connected components formed by all vocabularies.

Computing cache directly within the webservice is not possible because Hugging Face Datasets does not have Java API.
Common cache store such as Redis is overkill because this cache is going to be read-only.
The best option is then a file-based cache

### Computing Cache

Since [wilhelm-vocabulary](https://github.com/QubitPi/wilhelm-vocabulary) is a highly personalized and __manually-made
data set__, it is safe to assume the datasize won't be large. In fact, its no more than tens of thousands of nodes. This
allows for simpler cache loading algorithm which is easier to maintain

Development
-----------

### Environment Setup

Get the source code:

```console
git clone git@github.com:QubitPi/Antiqua.git
cd graph-database-loader
```

It is strongly recommended to work in an isolated environment. Install virtualenv and create an isolated Python
environment by

```console
python3 -m pip install --user -U virtualenv
python3 -m virtualenv .venv
```

To activate this environment:

```console
source .venv/bin/activate
```

or, on Windows

```console
./venv\Scripts\activate
```

> [!TIP]
>
> To deactivate this environment, use
>
> ```console
> deactivate
> ```

### Installing Dependencies

```console
pip3 install -r requirements.txt
```

### Pushing a New Tag For Release

The CI/CD [publishes Graph Database Loader to PyPi](https://pypi.org/project/graph-database-loader/). This relies on
the tag

To create the tag (`0.0.1` for example):

```console
git tag -a 0.0.1 -m "0.0.1"
git push origin 0.0.1
```

License
-------

The use and distribution terms for [Wilhelm Graph Database Python SDK]() are covered by the
[Apache License, Version 2.0].

[Apache License badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License URL]: https://www.apache.org/licenses/LICENSE-2.0
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0.html

[GitHub Workflow Status badge]: https://img.shields.io/github/actions/workflow/status/QubitPi/Antiqua/graph-database-loader-ci-cd.yaml?logo=github&style=for-the-badge&label=CI/CD
[GitHub Workflow Status URL]: https://github.com/QubitPi/Antiqua/actions/workflows/graph-database-loader-ci-cd.yaml

[Python Version Badge]: https://img.shields.io/badge/Python-3.10-brightgreen?style=for-the-badge&logo=python&logoColor=white
[PyPI project badge]: https://img.shields.io/pypi/v/graph-database-loader?logo=pypi&logoColor=white&style=for-the-badge
[PyPI project url]: https://pypi.org/project/graph-database-loader/

[Read the Docs badge]: https://img.shields.io/readthedocs/graph-database-loader?style=for-the-badge&logo=readthedocs&logoColor=white&label=Read%20the%20Docs&labelColor=8CA1AF
[Read the Docs URL]: https://sdk.wilhelmlang.com

[wilhelmlang.com]: https://wilhelmlang.com/
