from functools import reduce

"""Develop a function that computes the sum of a list of integers using the reduce predifined function."""

def sum_of_list(lst):
    output = 0
    for element in lst:
        output += element
    return output




lst = [1,1,1,1,2,]

summe = reduce((lambda x, y: x+y), lst)

print(summe)




