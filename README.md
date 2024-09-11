Wilhelm Vocabulary
==================

The data that serves [wilhelmlang.com](https://wilhelmlang.com/). The data is written in YAML format, because

1. it is machine-readable so that it can be consumed quickly in data pipelines
2. it is human-readable and, thus, easy to modify
3. it supports multi-lines value which is very handy for data of natural languages

YAML Schema
-----------

### Geraman

```yaml
vocabulary:
  - term: string
    definition: list
    plural: string
    declension/conjugation: string
```

### Korean

TBA

### Ancient Greek

TBA

### Latin

TBA
