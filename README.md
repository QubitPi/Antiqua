Wilhelm Vocabulary
==================

[![GitHub workflow status badge][GitHub workflow status badge]][GitHub workflow status URL]
[![Apache License Badge]][Apache License, Version 2.0]

<!-- TOC -->

- [Wilhelm Vocabulary](#wilhelm-vocabulary)
  - [Data Format](#data-format)
    - [Encoding Table in YAML](#encoding-table-in-yaml)
  - [Data Pipeline](#data-pipeline)
  - [How Data (Vocabulary) is Stored in a Graph Database](#how-data-vocabulary-is-stored-in-a-graph-database)
    - [Why Graph Database](#why-graph-database)
    - [Base Schema](#base-schema)
    - [Inflections](#inflections)
    - [Basic Graph Query](#basic-graph-query)
  - [Languages](#languages)
    - [German](#german)
      - [Noun Declension](#noun-declension)
        - [Declension Templates](#declension-templates)
          - [Masculine](#masculine)
          - [Feminine](#feminine)
          - [Neuter](#neuter)
      - [(Attributive) Adjective Declension](#attributive-adjective-declension)
      - [Pronoun Declension](#pronoun-declension)
      - [Verb Conjugation](#verb-conjugation)
    - [Ancient Greek](#ancient-greek)
      - [Diacritic Mark Convention](#diacritic-mark-convention)
      - [Noun Declension](#noun-declension-1)
      - [Adjective Declension](#adjective-declension)
      - [Verb Conjugation](#verb-conjugation-1)
    - [Latin](#latin)
    - [Classical Hebrew (Coming Soon)](#classical-hebrew-coming-soon)
    - [Korean](#korean)
  - [License](#license)

<!-- TOC -->

Data Format
-----------

The data that serves [wilhelmlang.com](https://wilhelmlang.com/). They are written in YAML format, because

1. it is machine-readable so that it can be consumed quickly in data pipelines
2. it is human-readable and, thus, easy to read and modify
3. it supports multi-lines value which is very handy for language data

### Encoding Table in YAML

To encode the inflections which are common in most Indo-European languages, an
[application-specific YAML](https://stackoverflow.com/q/30894438/14312712) that looks like the following are employed
throughout this repository:

```yaml
  - term: der Kaufmann
    definition: (male) trader
    declension:
      - ["",         singular, singular, singular,                plural, plural                   ]
      - ["",         indef.,   def.,     noun,                    def.,   noun                     ]
      - [nominative, ein,      der,      Kaufmann,                die,    "Kaufmänner, Kaufleute"  ]
      - [genitive,   eines,    des,      "Kaufmannes, Kaufmanns", der,    "Kaufmänner, Kaufleute"  ]
      - [dative,     einem,    dem,      Kaufmann,                den,    "Kaufmännern, Kaufleuten"]
      - [accusative, einen,    den,      Kaufmann,                die,    "Kaufmänner, Kaufleute"  ]
```

> [!NOTE]
>
> - A list under `declension` is a table row
> - All rows have the same number of columns
> - Each element of the list corresponds to a table cell

The declension (inflection) table above is equivalent to

<table><thead>
  <tr>
    <th></th>
    <th colspan="3">singular</th>
    <th colspan="2">plural</th>
  </tr></thead>
<tbody>
  <tr>
    <td></td>
    <td>indef.</td>
    <td>def.</td>
    <td>noun</td>
    <td>def.</td>
    <td>noun</td>
  </tr>
  <tr>
    <td>nominative</td>
    <td>ein</td>
    <td>der</td>
    <td>Kaufmann</td>
    <td>die</td>
    <td>Kaufmänner, Kaufleute</td>
  </tr>
  <tr>
    <td>genitive</td>
    <td>eines</td>
    <td>des</td>
    <td>Kaufmannes, Kaufmanns</td>
    <td>der</td>
    <td>Kaufmänner, Kaufleute</td>
  </tr>
  <tr>
    <td>dative</td>
    <td>einem</td>
    <td>dem</td>
    <td>Kaufmann</td>
    <td>den</td>
    <td>Kaufmännern, Kaufleuten</td>
  </tr>
  <tr>
    <td>accusative</td>
    <td>einen</td>
    <td>den</td>
    <td>Kaufmann</td>
    <td>die</td>
    <td>Kaufmänner, Kaufleute</td>
  </tr>
</tbody>
</table>

Data Pipeline
-------------

![Data pipeline](data-pipeline.png "Error loading data-loading.png")

How Data (Vocabulary) is Stored in a Graph Database
---------------------------------------------------

### Why Graph Database

Graph data representation assumes universal connectivity among world entities. This applies pretty well to the realm of
languages. Multilanguage learners have already seen that Indo-European languages are similar in many aspects. The
similarities not only signify the historical facts about Philology but also surface a great opportunity for
multilanguage learners to take advantages of them and study much more efficiently. What's missing is connecting the dots
using Graph Databases that visually presents these vastly enlightening links between the related languages in a natural
way.

### Base Schema

```yaml
vocabulary:
  - term: string
    definition: list
```

_The meaning of a word is called the `definition`_. A term has a natural relationship to its definition(s). For example,
the German noun "[Ecke](https://en.wiktionary.org/wiki/Ecke#Noun)" has at least 4 definitions:

![Relationship between term and defintion(s)](./definition.png "Error loading definition.png")

<div align="center">
    Graph data generated by <a href="https://github.com/QubitPi/wilhelm-python-sdk">wilhelm-python-sdk</a>
</div>

> [!TIP]
>
> The parenthesized value at the beginning of each `definition` item played an un-ignorable role: it is the label of the
> relationship between `term` and `definition` in graph database loaded by
> [Wilhelm SDK](https://github.com/QubitPi/wilhelm-python-sdk). For example, both German words
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

### Inflections

Indo-European languages are mostly inflected. The way inflections are encoded are documented for each language
separately:

- [German declension](#german-declension)
- [German conjugation](#german-conjugation)
- [Ancient Greek declension](#greek-declension)
- [Ancient Greek conjugation](#greek-conjugation)

### Basic Graph Query

- Search for a vocabulary with all its links:

  ```text
  MATCH (term:Term)-[r]-(x) WHERE term.name = "der Amerikaner" RETURN term, r, x;
  ```

Languages
---------

### [German](./german.yaml)

#### Noun Declension

__Declension__ is the inflection for nouns and adjectives.

> [!TIP]
>
> __The declension tables for all nouns are sourced from
> [Wiktionary](https://en.wiktionary.org/wiki/Kaufmann#Declension)__

##### Declension Template

`term` with a _definite article_ of __der__ signifies a __masculine noun__ which has a declension table template of the
following form:

```yaml
declension:
  - ["",         singular, plural]
  - ["",         noun,     noun  ]
  - [nominative, ████████, ██████]
  - [genitive,   ████████, ██████]
  - [dative,     ████████, ██████]
  - [accusative, ████████, ██████]
```

For example:

```yaml
  - term: das Getränk
    definition: the drink
    declension:
      - ["",         singular,            plural   ]
      - [nominative, Getränk,             Getränke ]
      - [genitive,   Getränkes, Getränks, Getränke ]
      - [dative,     Getränk,             Getränken]
      - [accusative, Getränk,             Getränke ]
```

> [!CAUTION]
>
> [Adjectival nouns](https://en.wikibooks.org/wiki/German/Grammar/Nouns/Adjectival_Nouns), however, do NOT follow the
> template above.

### [Ancient Greek](./ancient-greek.yaml)

Unless otherwise mentioned, we are talking about Attic Greek throughout this repository.

#### Diacritic Mark Convention

We employ the following 3 diacritic signs only in vocabulary:

1. the __acute__ (ά)
2. the __circumflex__ (ᾶ), and
3. the __grave__ (ὰ)

In fact, it is called the [_medium diacritics_](https://lsj.gr/wiki/%E1%BC%80%CE%B3%CE%B1%CE%B8%CF%8C%CF%82)  and the
same convention used in [Loeb Classical Library prints](https://ryanfb.xyz/loebolus/) from Harvard. Notice that,
however, the commonly sourced [Wiktionary uses full diacritics](https://en.wiktionary.org/wiki/%E1%BC%80%CE%B3%CE%B1%CE%B8%CF%8C%CF%82#Declension),
including the [breve diacritic mark](https://en.wikipedia.org/wiki/Breve); we don't do that.

#### Noun Declension

The vocabulary entry for each noun consists of its nominative and genitive forms, an article which indicates the noun's
gender, and the English meaning. For example.

```yaml
  - term: τέχνη τέχνης, ἡ
    definition:
      - art,
      - skill,
      - craft
    declension class: 1st
```

the vocabulary entry above consists of the following 4 items:

1. τέχνη: nominative singular
2. τέχνης: genitive singular
3. ἡ: nominative feminine singular of the article, which shows that the gender of the noun is feminine. Gender will be
   indicated by the appropriate form of the definite article "the":

   - ὁ for the masculine nouns
   - ἡ for the feminine nouns
   - τό for the neutor nouns

4. a list of English meanings of the word
5. the noun employs the first declension. The 3 classes of declensions are

   1. first declension (`1st`)
   2. second declension (`2nd`)
   3. third declension (`3rd`)

   A multi-form nouns will have a list for this field. For example

   ```yaml
     - term: αὐτός αὐτή αὐτό
       definition:
         - (without article) he, she, it, they
         - (without article) himself, herself, itself, themselves
         - (with definite article) same
       declension class:
         αὐτός: 2nd
         αὐτή: 1st
         αὐτό: 2nd
   ```

The declension of the entry is not shown because to decline any noun, we can take the genitive singular, remove the
genitive singular ending to get the stem, and then add the proper set of endings to the stem based on its declension
class[^2].

[^2]: _[Greek: An Intensive Course, 2nd Revised Edition](https://www.amazon.com/Greek-Intensive-Course-2nd-Revised/dp/0823216632)_, Hansen & Quinn, _p.20_

For example, to decline _τέχνη τέχνης, ἡ, art_, take the genitive singular _τέχνης_, remove the genitive singular ending
_-ης_, and add the appropriate endings to the stem which gives following paradigm:

|    Case    | Singular | Plural  |
|:----------:|:--------:|:-------:|
| nominative |  τέχνη   | τέχναι  |
|  genitive  |  τέχνης  | τεχνῶν  |
|   dative   |  τέχνῃ   | τέχναις |
| accusative |  τέχνην  | τέχνᾱς  |
|  vocative  |  τέχνη   | τέχναι  |

#### Adjective Declension

Declension template:

```yaml
declension:
  - ["",         singular,  singular, singular, dual,      dual,     dual    plural,    plural,   plural]
  - ["",         masculine, feminine, neuter,   masculine, feminine, neuter, masculine, feminine, neuter]
  - [nominative, █████████, ████████, ████████, █████████, ████████, ██████, █████████, ████████, ██████]
  - [genitive,   █████████, ████████, ████████, █████████, ████████, ██████, █████████, ████████, ██████]
  - [dative,     █████████, ████████, ████████, █████████, ████████, ██████, █████████, ████████, ██████]
  - [accusative, █████████, ████████, ████████, █████████, ████████, ██████, █████████, ████████, ██████]
  - [vocative,   █████████, ████████, ████████, █████████, ████████, ██████, █████████, ████████, ██████]
```

#### Verb Conjugation

The Greek verb has __6__ principal parts. All 6 must be learned whenever a new verb is encountered:

1. (first person singular) present indicative active
2. (first person singular) future indicative active
3. (first person singular) aorist indicative active
4. (first person singular) perfect indicative active
5. (first person singular) perfect indicative passive
6. (first person singular) aorist indicative passive

> [!TIP]
>
> The minimum number of forms which one must know in order to generate all possible forms of a verb are called the
> __principal parts__ of that verb.

From the 6 forms above, various verb forms (i.e. stems & endings) can be derived by rules[^4]

[^4]: _[Greek: An Intensive Course, 2nd Revised Edition](https://www.amazon.com/Greek-Intensive-Course-2nd-Revised/dp/0823216632)_, Hansen & Quinn, _p.44_

In practice, however,
[obtaining precise and complete principal parts for some verbs has been proven to be impossible](https://latin.stackexchange.com/a/17432).
While the best efforts have been made for reconstructing the complete principal parts, we also put a link to the
Wiktionary of each verb for
[wilhelm-python-sdk](https://sdk.wilhelmlang.com/en/latest/#module-wilhelm_python_sdk.ancient_greek_wiktionary_parser),
which will dynamically load the complete conjugation tables into graph database.

What's also being loaded are the reconstructed principal parts with a list of references that validate the
reconstruction.

In conclusion, the entry of a verb, thus, has the form of:

```yaml
- term: string
  definition: list
  conjugation:
    wiktionary: string
    principal parts:
      - ["",                                                 Attic, (Possibly other dialects)]
      - [(first person singular) present indicative active,  █████, ...                      ]
      - [(first person singular) future indicative active,   █████, ...                      ]
      - [(first person singular) aorist indicative active,   █████, ...                      ]
      - [(first person singular) perfect indicative active,  █████, ...                      ]
      - [(first person singular) perfect indicative passive, █████, ...                      ]
      - [(first person singular) aorist indicative passive,  █████, ...                      ]
    references: list
```

For example:

```yaml
  - term: λέγω
    definition:
      - to say, speak
      - to pick up
    conjugation:
      wiktionary: https://en.wiktionary.org/wiki/λέγω#Verb_2
      principal parts:
        - ["",                                                 Attic    , Koine          ]
        - [(first person singular) present indicative active,  λέγω     , λέγω           ]
        - [(first person singular) future indicative active,   λέξω     , ἐρῶ            ]
        - [(first person singular) aorist indicative active,   ἔλεξα    , εἶπον/εἶπα     ]
        - [(first person singular) perfect indicative active,  (missing), εἴρηκα         ]
        - [(first person singular) perfect indicative passive, λέλεγμαι , λέλεγμαι       ]
        - [(first person singular) aorist indicative passive,  ἐλέχθην  , ἐρρέθην/ἐρρήθην]
      references:
        - https://en.wiktionary.org/wiki/λέγω#Inflection
        - http://atticgreek.org/downloads/allPPbytypes.pdf
        - https://books.openbookpublishers.com/10.11647/obp.0264/ch25.xhtml
        - https://www.billmounce.com/greek-dictionary/lego
        - https://koine-greek.fandom.com/wiki/Λέγω
```

### [Latin](./latin.yaml)

```yaml
vocabulary:
  - term: string
    definition: list
```

### Classical Hebrew (Coming Soon)

The vocabulary is presented to help read and understand [Biblical Hebrew](https://mechon-mamre.org/p/pt/pt00.htm#mp3). A
[complementary audio](https://mechon-mamre.org/p/pt/ptmp3prq.htm) helps well with the pronunciation.

### [Korean](./korean.yaml)

中国人学习韩语有先天优势，加之韩语本身也是一门相当简单的语言，所以这里将语法和词汇合并在一起；
每一项也只由 `term`（韩）和 `definition`（中）组成，

```yaml
vocabulary:
  - term: string
    definition: list of strings
    example:
      - Korean: 제가 아무렴 그쪽 편에 서겠어요
        Chinese: 我无论如何都会站在你这边
      - Korean: ...
        Chinese: ...
```

不用费太多功夫记牢简单的语法和词汇，剩下的就是拿韩语字幕剧不停练习听说读写既成。`example` 中的例句均来自[韩国本土语料](https://www.amazon.com/Korean-book-%EB%82%98%EC%9D%98-%EC%95%84%EC%A0%80%EC%94%A8-%EC%A0%842%EA%B6%8C/dp/8933871756)

> [!NOTE]
>
> 韩语不属于汉藏语系，因其所属语系非常狭小，无法和其它语言产生足够关联，因此其数据暂时不被存入图数据库进行数据分析

License
-------

The use and distribution terms for [wilhelm-vocabulary]() are covered by the [Apache License, Version 2.0].

[Apache License Badge]: https://img.shields.io/badge/Apache%202.0-F25910.svg?style=for-the-badge&logo=Apache&logoColor=white
[Apache License, Version 2.0]: https://www.apache.org/licenses/LICENSE-2.0

[GitHub workflow status badge]: https://img.shields.io/github/actions/workflow/status/QubitPi/wilhelm-vocabulary/ci-cd.yaml?branch=master&style=for-the-badge&logo=github&logoColor=white&label=Database%20Loading
[GitHub workflow status URL]: https://github.com/QubitPi/wilhelm-vocabulary/actions/workflows/ci-cd.yaml
