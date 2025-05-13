#!/usr/bin/python3

def weight_average(my_list=[]):
    result = 0
    count = 0
    if len(my_list) == 0:
        return result
    for couple in my_list:
        result += couple[0] * couple[1]
        count += couple[1]

    return (float(result / count))

def main():
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))

main()
