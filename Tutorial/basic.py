import functools, operator


def list_len(lst):
    """
    Take a list of strings and returns a list of integer where
    the values are the lenght of each string
    """
    res_lst = []
    for s in lst:
        res_lst += [len(s)]
    return res_lst


def list_len_comp(lst):
    """
    Take a list of strings and returns a list of integer where
    the values are the lenght of each string
    """
    res_lst = [len(x) for x in lst]
    return res_lst


def map_dup(fun, lst):
    """
    Implementation of the map function, takes a function fun and
    applies it to every element of lst.
    """
    res_lst = []
    for s in lst:
        res_lst += [fun(s)]
    return res_lst


def map_yield(fun, it):
    """
    Implementation of the map function. it is an iterable, an object that
    has a __iter__ method which returns an iterator. Yield keyword
    is like return but return a generator.  This explain why
    the predefined function map need the use of list function
    to really produce a list.
    """
    for i in it:
        yield fun(i)


def sum_dup(lst):
    """Computes and return the sum of list"""
    s = 0
    for x in lst:
        s += x
    return s


def flat(lst_lst):
    """flats a list of lists without using any predefined functions."""
    res_lst = []
    for l in lst_lst:
        res_lst += l
    return res_lst



def main():
    """ Launcher """
    lst = ["hello", "world", "abc"]
    print(lst)

    print(list_len(lst))

    print(list_len_comp(lst))

    print(map_dup(len, lst))

    # the map predefined function return a generator not a list
    print(map_yield(len, lst))

    # it is necessary to use the list function to produce a list
    print(list(map_yield(len, lst)))

    # the map predefined function returns a generator not a list
    print(map(len, lst))

    # it is necessary to use the list function to produce a list
    print(list(map(len, lst)))

    print(sum_dup([2, 3, 4]))

    #Start here
    # sum of a list by means of reduce function
    adder = (lambda a, b: a + b)
    print(functools.reduce(adder, [2, 3, 4]))

    # sum of a list with predefined __add__ function/operator
    print(functools.reduce(operator.__add__, [2, 3, 4]))

    # sum of a list with optional initial value
    print(functools.reduce(operator.__add__, [2, 3, 4], 0))

    print(flat([[3, 8], [8, 9, 9], [1, 2]]))

    print(functools.reduce(operator.__add__, [[3, 8], [8, 9, 9], [1, 2]]))


if __name__ == "__main__":
    """main()"""
    b = 10
    for i in range(1,100):
        if i <= b:
            print("zahl ausgeben: " + str(i))
        else:
            break

