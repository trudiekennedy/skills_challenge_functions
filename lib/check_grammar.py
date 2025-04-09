def check_grammar(text):
    if text == "":
        raise Exception("No text to analyse!")
    return text[0].isupper() and text[-1] in ["!", "?", "."]