#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    result = 0
    count = 0
    for couple in my_list:
        result += couple[0] * couple[1]
        count += couple[1]

    return (result / count)
