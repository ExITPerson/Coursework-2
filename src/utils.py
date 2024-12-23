import json

def contains_any_words(content, words):
    return any(word.lower() in content.lower() for word in words)


def get_top_n(data, top_n):
    result = sorted(data, key=lambda x: (x["salary"]["from"], x["salary"]["to"]), reverse=True)
    return result[0:top_n]
