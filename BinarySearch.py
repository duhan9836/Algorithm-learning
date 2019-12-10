"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    l = len(input_array)
    start = 1
    end = l
    i = l // 2 + l % 2
    n = i

    while input_array[n - 1] != value and l > 1:
        if input_array[n - 1] > value:
            l = i - 1
            start = n - l
            end = n - 1
            i = l // 2 + l % 2
            n = start + i - 1
        else:
            l = l - i
            start = n + 1
            end = n + l
            i = l // 2 + l % 2
            n = n + i

    if input_array[n - 1] == value:
        return n - 1
    else:
        return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
test_val=[test_val1,test_val2]
for val in test_val:
    print ("the position for {} is {}".format(val,binary_search(test_list,val)))
