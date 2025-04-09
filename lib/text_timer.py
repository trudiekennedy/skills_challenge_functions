def find_reading_time(text):
    if text == "":
        raise Exception("No text given: nothing to calculate!")
    word_list = text.split()
    return (len(word_list)) / 200

