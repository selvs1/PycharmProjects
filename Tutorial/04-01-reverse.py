def reverseList(dataList):
    posCount = len(dataList)
    outputList = []
    for i in range(1, posCount + 1):
        outputList.append(dataList[-i])
    return outputList


def main():
    """ Launcher """
    #lst = list(input("Input a list: "))
    lst = [2, 3, 3, 3, 2, 5, 8, 9, 7, 5, 34, 345, 46, 57, 8, 8, 5, 34, 45, 3453456, 3456, 3456, 987654, 7, 7, 6, 6, 6, 6, 0]
    print("The reverse of \n {} \nis \n {}.".format(lst, reverseList(lst)))


if __name__ == "__main__":
    main()