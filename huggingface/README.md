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
      - split: Italian
        path: italian-graph-data.jsonl
      - split: Latin
        path: latin-graph-data.jsonl
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
