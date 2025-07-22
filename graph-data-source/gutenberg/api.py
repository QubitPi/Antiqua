import random

import genanki
import requests
from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')
db = client.db("wiktionary", username='root', password='no-password')
collection = db.collection('German')

model = genanki.Model(
    random.randrange(1 << 30, 1 << 31),
    'German Vocabulary',
    fields=[
        {'name': 'German'},
        {'name': 'Translation'},
        {'name': 'Rank'},
        {'name': 'Count'}
    ],
    templates=[
        {
            'name': 'German to English',
            'qfmt': '<div style="font-size: 32px;">{{German}}</div>',
            'afmt': '''{{FrontSide}}<hr id="answer">
<div style="font-size: 24px; margin: 20px 0;">{{Translation}}</div>
<div style="font-size: 14px; color: #666; margin-top: 20px;">
Rank: {{Rank}} | Occurrences: {{Count}}
</div>''',
        }
    ],
    css='''
            .card {
                font-family: 'Poppins', Arial, sans-serif;
                font-size: 20px;
                text-align: center;
                color: black;
                background-color: white;
                padding: 20px;
            }
            '''
)

deck = genanki.Deck(random.randrange(1 << 30, 1 << 31), "Kritik der reinen Vernunft")


def get_book_txt_by_url(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the file: {e}")


def get_unique_terms(text: str) -> list:
    import spacy
    nlp = spacy.load("de_core_news_sm")
    nlp.max_length = len(text) + 1000
    doc = nlp(text)
    vocabulary = [
        token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop
    ]
    return list(set(vocabulary))


def extract_vocabularies(text: str):
    from collections import Counter

    vocabulary = get_unique_terms(text)

    counting_map = Counter(vocabulary)
    ranking_map = {pair[0]: rank for rank, pair in enumerate(counting_map.most_common())}

    for word in vocabulary:
        result = collection.find({"term": word})
        if result is None or len(result) <= 0:
            print("{} has no matching defs".format(word))
        for doc in result:
            deck.add_note(
                genanki.Note(
                    model=model,
                    fields=[
                        word,
                        ", ".join(set(doc["definitions"])),
                        str(ranking_map[word]),
                        str(counting_map[word])
                    ]
                )
            )

    genanki.Package(deck).write_to_file("Kant-Critique-of-Pure-Reason.apkg")


if __name__ == "__main__":
    extract_vocabularies(get_book_txt_by_url("https://www.gutenberg.org/files/6342/6342-8.txt"))
