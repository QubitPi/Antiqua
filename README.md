Wilhelm Vocabulary
==================

![GitHub last commit badge][GitHub last commit]
![GitHub workflow status badge][GitHub workflow status]
[![Apache License Badge]](https://www.apache.org/licenses/LICENSE-2.0)

<!-- TOC -->
* [Wilhelm Vocabulary](#wilhelm-vocabulary)
  * [YAML Schema](#yaml-schema)
    * [German](#german)
    * [Korean](#korean)
    * [Classical Hebrew (Coming Soon)](#classical-hebrew-coming-soon)
    * [Ancient Greek](#ancient-greek)
    * [Latin](#latin)
  * [License](#license)
<!-- TOC -->

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

- The declension/conjugation table employees an
  [application-specific YAML](https://stackoverflow.com/q/30894438/14312712) that looks like the following:

  ```yaml
    - term: ein
      definition: (article) a, an
      declension:
        - [-         , masculine, feminine, neuter, plural]
        - [nominative, ein,       eine,     ein,    -     ]
        - [genitive,   eines,     einer,    eines,  -     ]
        - [dative,     einem,     einer,    einem,  -     ]
        - [accusative, einen,     eine,     ein,    -     ]
  ```

  The declension table is equivalent to

  |                | masculine | feminine | neuter | plural |
  |:--------------:|:---------:|:--------:|:------:|:------:|
  | __nominative__ |    ein    |   eine   |  ein   |  N/A   |
  |  __genitive__  |   eines   |  einer   | eines  |  N/A   |
  |   __dative__   |   einem   |  einer   | einem  |  N/A   |
  | __accusative__ |   einen   |   eine   |  ein   |  N/A   |

  __The declension/conjugation tables for all vocabularies are sourced from
  [Wiktionary](https://en.wiktionary.org/wiki/ein#Declension_2)__

### [Korean](./korean.yaml)

中国人学习韩语有先天优势，加之韩语本身也是一门相当简单的语言， 所以这里将语法和词汇合并在一起；
每一项也只由 `term`（韩）和 `definition`（中）组成，

```yaml
vocabulary:
  - term: string
    definition: list
```

### Classical Hebrew (Coming Soon)

The vocabulary is presented to help read and understand [Biblical Hebrew](https://mechon-mamre.org/p/pt/pt00.htm#mp3). A
[complementary audio](https://mechon-mamre.org/p/pt/ptmp3prq.htm) helps well with the pronunciation.

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
