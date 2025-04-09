def find_reading_time(text):
    if text == "":
        return "No text given: nothing to calculate!"
    else: 
        word_list = text.split()
        return (len(word_list)) / 200

