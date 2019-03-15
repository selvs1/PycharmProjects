"""

Develop a function that takes a list of strings and returns a list of integers where the elements are the length of the corresponding string. Do not use any predefined functions.
Example: lst_len(["abc", "de", "fghi"]) returns [3,2,4]"""

lst = ["abc", "de", "fghi"]


def lst_len(lst):
    output = []
    for e in lst:
        output.append(len(e))
    return output

print(lst_len(lst))