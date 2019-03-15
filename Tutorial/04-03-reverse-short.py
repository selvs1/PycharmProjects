def reverseListLit(dataList):
    return dataList[::-1]

def main():
    """ Launcher """
    #lst = list(input("Input a list: "))
    lst = [2, 3, 3, 3, 2, 5, 8, 9, 7, 5, 34, 345, 46, 57, 8, 8, 5, 34, 45, 3453456, 3456, 3456, 987654, 7, 7, 6, 6, 6, 6, 0]

    print("The reverse of {} is {}.".format(lst, reverseListLit(lst)))


if __name__ == "__main__":
    main()