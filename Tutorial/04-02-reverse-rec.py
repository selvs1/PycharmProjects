def reverse_rec(lst):
    """Reverse a given list of elements (recursive version)"""

    if lst == []:
        return []
    else:
        head, tail = lst[0], lst[1:]
        return reverse_rec(tail) + [head]


def main():
    """ Launcher """
    #lst = list(input("Input a list: "))
    lst = [2, 3, 3, 3, 2, 5, 8, 9, 7, 5, 34, 345, 46, 57, 8, 8, 5, 34, 45, 3453456, 3456, 3456, 987654, 7, 7, 6, 6, 6, 6, 0]

    print("The reverse of {} is {}.".format(lst, reverse_rec(lst)))


if __name__ == "__main__":
    main()