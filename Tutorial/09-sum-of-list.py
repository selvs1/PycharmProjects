"""Develop a function that computes the sum of a List of integers without using any predefined functions."""

lst = [1,1,1,1,1,2]

def sum_of_list(lst):
    output = 0
    for element in lst:
        output += element
    return output

print(sum_of_list(lst))

