#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = text.replace(". ", ".").replace("? ", "?").replace(": ", ":")

    for i in new:
        if i == '.' or i == '?' or i == ':':
            print("{}\n".format(i))
        else:
            print("{}".format(i), end="")
