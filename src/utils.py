import json

def contains_any_words(content, words):
    return any(word.lower() in content.lower() for word in words)


def content_id(data, content):
        id_list = []
        for x in data:
            id_list.append(x["id"])
        return bool(content in id_list)

def get_top_n(data, top_n):
    result = sorted(data, key=lambda x: (x["salary"]["from"], x["salary"]["to"]))
    return result[0:top_n]
