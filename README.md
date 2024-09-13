Wilhelm Vocabulary
==================

![GitHub last commit badge][GitHub last commit]
![GitHub workflow status badge][GitHub workflow status]
[![Apache License Badge]](https://www.apache.org/licenses/LICENSE-2.0)

The data that serves [wilhelmlang.com](https://wilhelmlang.com/). They are written in YAML format, because

1. it is machine-readable so that it can be consumed quickly in data pipelines
2. it is human-readable and, thus, easy to modify
3. it supports multi-lines value which is very handy for data of natural languages

YAML Schema
-----------

> [!TIP]
>
> The parenthesized value at the beginning of each `definition` item played an un-ignorable role: it is the label of the
> relationship between `term` and `defintion` in graph database loaded by
> [Wilhelm SDK](https://github.com/QubitPi/wilhelm-graphdb-python). For example, both German words
>
> ```yaml
> - term: denn
>   definition:
>     - (adv.) then, thus
>     - (conj.) because
> ```
>
> and
>
> ```yaml
>  - term: nämlich
>    definition:
>      - (adj.) same
>      - (adv.) namely
>      - (adv.) because
> ```
>
> can mean "because" acting as different types. This is visualized as follows:
>
> ![error loading example.png](./example.png)
>
> __Visualzing synonyms this way presents a big advantage to human brain__ who is exceedingly good at memorizing
> patterns

### [German](./german.yaml)

```yaml
vocabulary:
  - term: string
    definition: list
    plural: string
    declension/conjugation: string
```

- The `conjugation` is the inflection paradigm for a German verb and `declension` the inflection for nouns and
  adjectives. Only one of the two is present for a term.
- The type of the word can be inferred using the following rule

  - `term` with a _definite article_ of "der"/"die"/"das" and a field of `plural` that comes with it signifies a
    __noun__
  - Those with `conjugation` field denotes a __verb__; its definition also begins with an _indefinite form_, i.e.
    "to ..."
  - The rests are explicitly stated in the `definition` field. For example,

    ```yaml
      - term: ob
        definition:
          - (conj.) if
          - (conj.) whether
    ```

    means "ob" is a **conjunction** in this case and

    ```yaml
      - term: denn
        definition:
          - (adv.) then, thus
          - (conj.) because
    ```

    tells that "denn" can be __adverb__ or __conjunction__

### [Korean](./korean.yaml)

```yaml
vocabulary:
  - term: string
    definition: list
```

### [Ancient Greek](./greek.yaml)

```yaml
vocabulary:
  - term: string
    definition: list
```

### [Latin](./latin.yaml)

```yaml
vocabulary:
  - term: string
    definition: list
```

License
-------

The use and distribution terms for [wilhelm-vocabulary]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: http://www.apache.org/licenses/LICENSE-2.0.html

[GitHub last commit]: https://img.shields.io/github/last-commit/QubitPi/wilhelm-vocabulary/master?logo=github&style=for-the-badge
[GitHub workflow status]: https://img.shields.io/github/actions/workflow/status/QubitPi/wilhelm-vocabulary/ci-cd.yaml?branch=master&logo=github&style=for-the-badge
