import json

def contains_any_words(content, words):
    return any(word.lower() in content for word in words)


def content_id(data, content):
    # with open(f"data/{file_name}.json", "r", encoding="utf-8") as f:
    #     data = json.load(f)
        id_list = []
        for x in data:
            id_list.append(x["id"])
        return bool(content in id_list)
