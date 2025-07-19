---
license: apache-2.0
pretty_name: Antiqua
language:
  - en
  - de
  - it
  - la
  - grc
configs:
  - config_name: Graph Data
    data_files:
      - split: German
        path: german-graph-data.jsonl
      - split: Latin
        path: latin-graph-data.jsonl
      - split: Italian
        path: italian-graph-data.jsonl
      - split: AncientGreek
        path: ancient-greek-graph-data.jsonl
tags:
  - Natural Language Processing
  - NLP
  - Vocabulary
  - German
  - Italian
  - Latin
  - Ancient Greek
  - Knowledge Graph
size_categories:
  - 1K<n<10K
---

Antiqua Datasets
----------------

```python
from datasets import load_dataset
dataset = load_dataset("QubitPi/Antiqua")
```

> [!TIP]
> If `dataset = load_dataset("QubitPi/Antiqua")` throws an error, please upgrade the `datasets` package to its
> _latest version_

There are 4 splits we can choose from:

1. German

   ```python
   split = dataset["German"]
   ```

2. German

   ```python
   split = dataset["Italian"]
   ```

3. Latin

   ```python
   split = dataset["Latin"]
   ```

4. Ancient Greek

   ```python
   split = dataset["AncientGreek"]
   ```

To iterate the split for each triple of source node, target node, and link:

```python
graph = split.iter(batch_size=1)
for triple in graph:
    source_node = {k: v for k, v in triple["source"][0].items() if v}
    target_node = {k: v for k, v in triple["target"][0].items() if v}
    link        = triple["link"][0]
```

Each `source_node` have the following fields (those in __bold__ exist in all nodes while others are not always present)

- __label__: the vocabulary term
- __language__: the language of this term and is always one of the following values:

  - `German`
  - `Latin`
  - `Ancient Greek`

- audio: the link to the Wiktionary audio of this vocabulary
- declension-_i_-_j_: The declension entry in the _i_-th row and _j_-th column in declension table

  > [!TIP]
  >
  > To encode the inflections which are common in most Indo-European languages, a virtual inflection table that looks
  > like the following are employed (taking German noun "Gegenstand" as an example):
  >
  > ```
  > ["",         singular,                    plural      ]
  > [nominative, Gegenstand,                  Gegenstände ]
  > [genitive,   "Gegenstandes, Gegenstands", Gegenstände ]
  > [dative,     Gegenstand,                  Gegenständen]
  > [accusative, Gegenstand,                  Gegenstände ]
  > ```
  >
  > The declension (inflection) table above is equivalent to
  >
  > <table><tbody>
  >   <tr>
  >     <td></td>
  >     <td>singular</td>
  >     <td>plural</td>
  >   </tr>
  >   <tr>
  >     <td>nominative</td>
  >     <td>Gegenstand</td>
  >     <td>Gegenstände</td>
  >   </tr>
  >   <tr>
  >     <td>genitive</td>
  >     <td>Gegenstandes, Gegenstands</td>
  >     <td>Gegenstände</td>
  >   </tr>
  >   <tr>
  >     <td>dative</td>
  >     <td>Gegenstand</td>
  >     <td>Gegenständen</td>
  >   </tr>
  >   <tr>
  >     <td>accusative</td>
  >     <td>Gegenstand</td>
  >     <td>Gegenstände</td>
  >   </tr>
  > </tbody>
  > </table>
  >
  > This has been encoded in Antiqua Hugging Face Datasets as:
  >
  > - declension-0-0 = ""
  > - declension-0-1 = "singular"
  > - declension-0-2 = "plural"
  > - declension-1-0 = "nominative"
  > - declension-1-1 = "Gegenstand"
  > - declension-1-2 = "Gegenstände"
  > - declension-2-0 = "genitive"
  > - declension-2-1 = "Gegenstandes, Gegenstands"
  > - ...
  > - declension-4-2 = "Gegenstände"

For example, to get the word and language of this word:

```python
graph = split.iter(batch_size=1)
for triple in graph:
    source_node = {k: v for k, v in triple["source"][0].items() if v}
    print("label: {label}".format(label=source_node["label"]))
    print("language: {language}".format(language=source_node["language"]))
```

Each `target_node` is either

- an object with the same field scheme as `source_node`, or
- a "definition" node with a non-null "label" field only, in which case, the "label" field is the English meaning of the
  word represented by the `source_node` pointing at this `target_node`

```python
graph = split.iter(batch_size=1)
for triple in graph:
    target_node = {k: v for k, v in triple["target"][0].items() if v}
    if target_node["language"] is None:
        print("This is an English definition of some source node word: {definition}".format(definition=target_node["label"]))
    else:
        print("label: {label}".format(label=target_node["label"]))
        print("language: {language}".format(language=target_node["language"]))
```

> [!TIP]
>
> In the case of a "definition" node, we will see all fields are `null` except for the "label" field. Why are there so
> many unnecessary null-fields? Because there are decent amount fo target nodes that are not "definition" nodes; these
> are source nodes themselves acting as target nodes because they have been spotted to have connections with other words

Each `link`, no surprises there, encodes the relationship between the `source_node` and `target_node`. Its __label__
field signifies the nature of the relationship. For example, `{ "label": "definition" }` means that `target_node` is the
definition of `source_node`

```python
graph = dataset[split].iter(batch_size=1)
for triple in graph:
    link = triple["link"][0]
    print(link["label"])
```
