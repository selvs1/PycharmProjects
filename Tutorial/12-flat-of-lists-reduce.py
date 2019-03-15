from functools import reduce

"""
Develop a function that flats a list of lists using the reduce predefined functions.

Example: flat([[3,8],[8,9,9],[1,2]]) returns [3,8,8,9,9,1,2]

"""
list_of_menuitems = [[3, 8], [8, 9, 9], [1, 2]]



"""tschegge nid..."""
liste = (map(lambda x: list(x),list_of_menuitems))
liste_done =(reduce(list.__add__, liste))

print(liste_done)