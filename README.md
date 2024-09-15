Wilhelm Vocabulary
==================

![GitHub last commit badge][GitHub last commit]
![GitHub workflow status badge][GitHub workflow status]
[![Apache License Badge]](https://www.apache.org/licenses/LICENSE-2.0)

The data that serves [wilhelmlang.com](https://wilhelmlang.com/). They are written in YAML format, because

1. it is machine-readable so that it can be consumed quickly in data pipelines
2. it is human-readable and, thus, easy to modify
3. it supports multi-lines value which is very handy for data of natural languages

[German](./german.yaml)
-----------------------

### YAML Schema

```yaml
vocabulary:
  - term: string
    definition: list
    plural: string
    declension/conjugation: application-specific table
```

- The `conjugation` is the inflection paradigm for a German verb and `declension` the inflection for nouns and
  adjectives. Only one of the two is present for a term.
- The type of the word can be inferred using the following rule

    - `term` with a _definite article_ of __der__/__die__/__das__ signifies a __noun__. For instance

      ```yaml
        - term: die Wissenschaft
          definition: the Science
      ```

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

### German Noun Declension

The declension table employees an [application-specific YAML](https://stackoverflow.com/q/30894438/14312712) that looks like the following:

```yaml
  - term: ein
    definition: (article) a, an
    declension:
      - ["",         masculine, feminine, neuter, plural]
      - [nominative, ein,       eine,     ein,    N/A   ]
      - [genitive,   eines,     einer,    eines,  N/A   ]
      - [dative,     einem,     einer,    einem,  N/A   ]
      - [accusative, einen,     eine,     ein,    N/A   ]
```

The declension table above is equivalent to

|                | masculine | feminine | neuter | plural |
|:--------------:|:---------:|:--------:|:------:|:------:|
| __nominative__ |    ein    |   eine   |  ein   |  N/A   |
|  __genitive__  |   eines   |  einer   | eines  |  N/A   |
|   __dative__   |   einem   |  einer   | einem  |  N/A   |
| __accusative__ |   einen   |   eine   |  ein   |  N/A   |

> [!NOTE]  
> - A list under `declension` is a table row
> - All rows have the same number of columns
> - Each element of the list corresponds to a table cell

> [!TIP]
> __The declension tables for all nouns are sourced from
> [Wiktionary](https://en.wiktionary.org/wiki/ein#Declension_2)__

### German Verb Conjugation

There are __3__ persons, __2__ numbers, and __4__ moods (indicative, conditional, imperative and subjunctive) to
consider in conjugation. There are __6__ tenses in German: the present and past are conjugated, and there are four
compound tenses. There are two categories of verbs in German:
[weak and strong](https://en.wikipedia.org/wiki/Germanic_strong_verb)[^1]. In addition,
[strong verbs are grouped into 7 "classes"](https://en.wikipedia.org/wiki/Germanic_strong_verb#Strong_verb_classes)

[^1]: https://en.wikipedia.org/wiki/German_verbs#Conjugation

The conjugation table of German verb on Wiktionary is hard to interpret as a German language learner. It does, however,
presents a very good Philology reference. For example, it tells us which of the 7 "classes" a strong verb belongs to.
__We, therefore, leave the Wiktionary links to the conjugation table of that verb for data processing in the future__,
for example,

```yaml
  - term: aufwachsen
    definition: to grow up
    conjugation: https://en.wiktionary.org/wiki/aufwachsen#Conjugation
```

and advise user to employ a much more practical method to learn daily conjugation as follows. We take __aufwachsen__ as
an example.

> [!IMPORTANT]  
> I'm not advertising for any organizations. I'm simply sharing good resources.

[Netzverb Dictionary](https://www.verbformen.com/) is the best German dictionary _targeting the vocabulary inflection_.
[Search for "aufwachsen"](https://www.verbformen.com/?w=aufwachsen) and we will see much more intuitive conjugation
tables listed.

This pretty much serves our needs, but what makes Netzverb unpenetrable by other dictionaries is that _every_ verb comes
with

1. [A printable version that looks much better than the browser's Control+P export](https://www.verbformen.com/conjugation/aufwachsen.pdf)

   - A "Sentences with German verb aufwachsen" section with a
     [link](https://www.verbformen.com/conjugation/examples/aufwachsen.htm) that offer a fruitful number of conjugated
     examples that get us familiar with the inflections of the verb

2. [An on-the-fly generated flashcard sheet](https://www.verbformen.com/conjugation/worksheets-exercises/lernkarten/aufwachsen.pdf)
   which allows us to make a better usage of our random free time
3. [A YouTube video that offers audios of almost every conjugated form](https://www.youtube.com/watch?v=LCtUrSn030A),
   which helps with conjugated pronunciations.

[Korean](./korean.yaml)
-----------------------

中国人学习韩语有先天优势，加之韩语本身也是一门相当简单的语言，所以这里将语法和词汇合并在一起；
每一项也只由 `term`（韩）和 `definition`（中）组成，

```yaml
vocabulary:
  - term: string
    definition: list
```

不用费太多功夫记牢简单的语法和词汇，剩下的就是拿韩语字幕剧不停练习听说读写既成。

Classical Hebrew (Coming Soon)
------------------------------

The vocabulary is presented to help read and understand [Biblical Hebrew](https://mechon-mamre.org/p/pt/pt00.htm#mp3). A
[complementary audio](https://mechon-mamre.org/p/pt/ptmp3prq.htm) helps well with the pronunciation.

[Ancient Greek](./greek.yaml)
-----------------------------

```yaml
vocabulary:
  - term: string
    definition: list
```

[Latin](./latin.yaml)
---------------------

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
