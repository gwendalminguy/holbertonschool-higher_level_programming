#!/usr/bin/python3
def remove_char_at(str, n):
    length = len(str)
    string = str
    if n < length and n >= 0:
        string = string[:n] + string[n+1:]
    return (string)
