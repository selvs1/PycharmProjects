def insertNumberInList(zahl, liste):
    found = 0
    pointer = 0
    oldArrayLength = len(liste)

    for i in range(len(liste)):
        if zahl < liste[i]:
            if found == 0:
                found = 1
                pointer = i - 1
        elif zahl == liste[i]:
            if found == 0:
                found = 1
                pointer = i
        elif zahl > liste[i]:
            if found == 0:
                if i == len(liste) - 1:
                    print("ende")
                    liste.append(zahl)
                if zahl < liste[i + 1]:
                    found = 1
                    pointer = i
                elif zahl >= liste[i + 1]:
                    pointer = i
    #print("pointer: " + str(pointer + 1))

    if (oldArrayLength - len(liste)) == 0:
        #print("Liste wurde nicht erweitert")
        liste.insert(pointer + 1, zahl)

    return liste


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


def insert_ord_2(num, lst):
    """
    Insert at the right place a number num into an ordered list lst (ascending order).
    This version update the parameter list and is written in a more classic way.
    """

    if lst == []:
        return lst.insert(0, num)  # insert into empty list
    else:
        done = False
        index = 0
        while (not done and index < len(lst)):
            if num <= lst[index]:  # insert at the right place (before)
                lst.insert(index, num)
                done = True
            index += 1
        if not done:
            lst.append(num)  # insert at the end


def insert_ord_3(num, lst):
    """
    Takes a number num and an ordered list of integers.  Returns another ordered list of integers
    that contains num. This version does not update lst.
    """
    if lst == []:
        res_list = [num]
    elif num >= lst[len(lst) - 1]:  # check if num is greater than every thing
        res_list = lst + [num]
    else:
        for index in range(len(lst)):
            if num < lst[index]:  # check if num is smaller than the current position
                index += 1
                res_list = lst[:index - 1] + [num] + lst[index - 1:]
                break
    return res_list



def insert_sort_moesching(e, l):
    for i in range(len(l)):
        if e < l[i]:
            l.insert(i,e)
            return i
    l.append(e)
    return len(l)-1


def main():
    """ Launcher """
    rawData = [4, 5, 7, 3, 534, 67, 3, 3, 0, 0, 444, 4, 4, 44, 4, 212, 12, 2, 3, 4, 5, 6, 7, 8, 9]
    rawData.sort()
    lst = rawData[:]


    num = 9999999
    lst = rawData[:]


    print("Insert {} in {}".format(num, lst))
    insertNumberInList(num, lst)
    print("gives {}".format(lst))
    print

    lst = rawData[:]


    print("Insert {} in {}".format(num, lst))
    insert_ord_1(num, lst)
    print("gives {}".format(lst))
    print

    lst = rawData[:]


    print("Insert {} in {}".format(num, lst))
    insert_ord_2(num, lst)
    print("gives {}".format(lst))
    print

    lst = rawData[:]


    print("Insert {} in {}".format(num, lst))
    print("Gives {}".format(insert_ord_3(num, lst)))
    print

    lst = rawData[:]


    print("@@@@@@")
    print("Insert {} in {}".format(num, lst))
    insert_sort_moesching(num, lst)
    print("gives {}".format(lst))
    print



if __name__ == "__main__":
    main()
