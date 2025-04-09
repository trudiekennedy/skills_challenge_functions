def count_words(text):
    if text == "":
        return 0
    word_list = text.split()
    return len(word_list)

