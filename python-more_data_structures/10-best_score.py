#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = 0
    name = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > highest:
            highest = a_dictionary[key]
            name = key
    return name

def main():
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))

main()
