""""
Develop a function that flats a list of lists without using any predefined functions.

Example: flat([[3,8],[8,9,9],[1,2]]) returns [3,8,8,9,9,1,2]
"""

lst = [[3, 8], [8, 9, 9], [1, 2]]


def flat(lst):
    output = []
    for element in lst:
        for subelement in element:
            output.append(subelement)
    return output

print(flat(lst))