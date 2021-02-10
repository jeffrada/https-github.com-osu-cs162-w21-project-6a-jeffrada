# Author: Adam Jeffries
# Date: 2/9/2021
# Description: A recursive function named list_max that takes as its parameter
# a list of numbers and returns the maximum value in the list.

def list_max(list):
    if len(list) == 1:
        print('length = 1, returning 1', list[0])
    m = list_max(list[1:])
    if m > list[0]:
        return m
    else:
        return list[0]
