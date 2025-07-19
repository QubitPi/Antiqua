import json


def json_to_jsonl(json_input: str, jsonl_output: str):
    with open(json_input, 'r') as input_file:
        data = json.load(input_file)
        with open(jsonl_output, 'w') as output_file:
            for triple in data:
                output_file.write(json.dumps(triple) + '\n')


if __name__ == "__main__":
    json_to_jsonl("../graph-json-generator/latin-graph-data.json", "latin-graph-data.jsonl")
    json_to_jsonl("../graph-json-generator/italian-graph-data.json", "italian-graph-data.jsonl")
    json_to_jsonl("../graph-json-generator/ancient-greek-graph-data.json", "ancient-greek-graph-data.jsonl")
    json_to_jsonl("../graph-json-generator/german-graph-data.json", "german-graph-data.jsonl")
