def greatestVal(list):
    greatestValue = list[0]
    for element in list:
        if element > greatestValue:
            greatestValue = element
    return greatestValue


def main():
    """ Launcher """
    lst = [2, 3, 3, 3, 2, 5, 8, 9, 7, 5, 34, 345, 46, 57, 8, 8, 5, 34, 45, 3453456, 3456, 3456, 987654, 7, 7, 6, 6, 6, 6, 0]
    #lst = list(input("Input a list of positive integers: "))
    print('The greatest element is {}.'.format(greatestVal(lst)))


if __name__ == "__main__":
    main()
