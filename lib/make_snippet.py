def make_snippet(text):
    text_list = text.split(" ")
    if len(text_list) > 5:
        first_five = text_list[0:5]
        snippet = " ".join(first_five)
        return snippet + "..."
    else:
        return text