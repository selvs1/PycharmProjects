"""

Develop a function that takes a list of strings and returns a list of integers where the elements are the length of the corresponding string. Do not use any predefined functions.
Example: lst_len(["abc", "de", "fghi"]) returns [3,2,4]"""

lst = ["abc", "de", "fghi"]


def lst_len_map(lst):
    return list(map(lambda x: len(x),lst))

print(lst_len_map(lst))

