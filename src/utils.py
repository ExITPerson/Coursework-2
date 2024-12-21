def contains_any_words(content, words):
    return any(word.lower() in content for word in words)