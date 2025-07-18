Graph Database Loader
=====================

[![PyPI][PyPI project badge]][PyPI project url]

Being a standalone subproject of Antiqua, __[Graph Data Loader](https://pypi.org/project/graph-database-loader/)__ is a
bundle of data pipeline that reads Antiqua's vocabulary from supported data sources and loads them into graph databases

Some features can be reused as SDK which can be installed via

```console
pip install graph-database-loader
```

Details documentations can be found at [antiqua.qubitpi.org](https://antiqua.qubitpi.org)

[//]: # (Wilhelm Vocabulary Loader)

[//]: # (-------------------------)

[//]: # ()
[//]: # (> [!CAUTION])

[//]: # (>)

[//]: # (> When the graph database is Neo4J, all constrains relating to the __Term__ node must be using:)

[//]: # (>)

[//]: # (> ```cypher)

[//]: # (> SHOW CONSTRAINTS)

[//]: # (> DROP CONSTRAINT constraint_name;)

[//]: # (> ```)

[//]: # (>)

[//]: # (> This is because certain vocabulary has multiple grammatical forms. This vocabulary is spread out as multiple entries.)

[//]: # (> These multiple entries, because they have lots of common properties, often triggers constraint violations in Neo4J on)

[//]: # (> load)

[//]: # ()
[//]: # (The absolute fastest way &#40;by far&#41; to load large datasets into neo4j is to use the bulk loader)

[//]: # ()
[//]: # (The cache here is defined as the set of all connected components formed by all vocabularies.)

[//]: # ()
[//]: # (Computing cache directly within the webservice is not possible because Hugging Face Datasets does not have Java API.)

[//]: # (Common cache store such as Redis is overkill because this cache is going to be read-only.)

[//]: # (The best option is then a file-based cache)

[//]: # ()
[//]: # (### Computing Cache)

[//]: # ()
[//]: # (Since [wilhelm-vocabulary]&#40;https://github.com/QubitPi/wilhelm-vocabulary&#41; is a highly personalized and __manually-made)

[//]: # (data set__, it is safe to assume the datasize won't be large. In fact, its no more than tens of thousands of nodes. This)

[//]: # (allows for simpler cache loading algorithm which is easier to maintain)

[//]: # ()
[//]: # (Wiktionary Data Loader &#40;Arango DB&#41;)

[//]: # (----------------------------------)

[//]: # ()
[//]: # ([graph-database-loader]&#40;&#41; works naturally for single-tenant application, the [wilhelmlang.com]. In order to support)

[//]: # (cross-language inferencing, all data are hence loaded into a __single__)

[//]: # ([Database]&#40;https://arango.qubitpi.org/stable/concepts/data-structure/#databases&#41;. Data of each langauge resides in)

[//]: # (dedicated [Collections]&#40;https://arango.qubitpi.org/stable/concepts/data-structure/#collections&#41;)

[//]: # ()
[//]: # (There are _n + 2_ Collections loaded:)

[//]: # ()
[//]: # (- _n_ document collections for n languages supported by [wiktionary-data]&#40;https://github.com/QubitPi/wiktionary-data&#41;)

[//]: # (- _1_ document collection for "Definition" entity, where the English definition of each word resides in one)

[//]: # (  [document]&#40;https://arango.qubitpi.org/stable/concepts/data-structure/#documents&#41;)

[//]: # (- _1_ edge collection for connections between words and definitions as well as those among words themselves)

[//]: # ()
[//]: # (> [!TIP])

[//]: # (>)

[//]: # (> See [_Collection Types_]&#40;https://arango.qubitpi.org/stable/concepts/data-structure/collections/#collection-types&#41; for)

[//]: # (> differences between document & edge collections)

[//]: # ()
[//]: # (Each collection generates index on the word term. If the term comes with a gender modifier, such as)

[//]: # ("das Audo" &#40;_car_, in German&#41;, a new)

[//]: # ([computed attribute]&#40;https://arango.qubitpi.org/stable/concepts/data-structure/documents/computed-values/&#41; that has)

[//]: # (the modifier stripped-off is used for indexing instead)

### Releasing Graph Database Loader

The CI/CD [publishes Graph Database Loader to PyPI](https://pypi.org/project/graph-database-loader/). This relies on
the currently latest [tag](https://github.com/QubitPi/Antiqua/tags) by incrementing the _patch_ version each time the
publish process runs.

The _major_ and _minor_ versions, however, have to be manually incremented. Whenever there is a need to do so (changing
`1.2.3` to `1.3.0`, for example), run __on master branch__ the following:

```console
git tag -a 1.3.0 -m "1.3.0"
git push origin 1.3.0
```

before merging the new-release PR and the new version 1.3.1 will come up after the PR is merged and released.

Development
-----------

### Environment Setup

Get the source code:

```console
git clone git@github.com:QubitPi/Antiqua.git
cd Antiqua/graph-database-loader
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

[PyPI project badge]: https://img.shields.io/pypi/v/graph-database-loader?logo=pypi&logoColor=white&style=for-the-badge&labelColor=7B99FA&color=53CDD8
[PyPI project url]: https://pypi.org/project/graph-database-loader/
