def insert_ord_1(num, lst):
    """
    Insert at the right place a number num into an ordered list lst (ascending order).
    This version update the parameter list and is written in a pythonic way.
    """

    if not lst:  # check if the list is empty
        return lst.insert(0, num)  # insert num
    else:
        if num >= lst[len(lst) - 1]:  # check if num is greater than every thing
            lst.append(num)  # append num to the list (after all the elements)
        else:
            for index in range(len(lst)):  # loop over the whole list
                if num <= lst[index]:  # check if num is smaller than the current position
                    lst.insert(index, num)  # insert before
                    break  # quit the for loop


def iSort(unsortedList):
    newList = []
    for element in unsortedList:
        insert_ord_1(element, newList)

    diniMuetter = newList
    return diniMuetter

diniMuetter = [4, 5, 7, 3, 534, 67, 3, 3, 0, 0, 0, 0, 0, 0, 444, 44, 4, 4, 4, 44, 4, 212, 12, 2, 3, 4, 5, 6, 7, 8, 9]

print(iSort(diniMuetter))