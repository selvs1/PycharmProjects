def even(b):
    """Return True if b is even"""
    if b % 2 == 0:
        return True
    else:
        return False

def e2(b):
    """Return True if b is even"""
    return b % 2 == 0

def main():
    """ Launcher """
    num = int(input("Input a number: "))
    if even(num):
        print('{} is even.'.format(num))
    else:
        print('{} is odd.'.format(num))

if __name__ == "__main__":
    main()