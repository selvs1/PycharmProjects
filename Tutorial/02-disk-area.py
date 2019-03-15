
import math
def diskarea(radius):
    """Computes the area of a disc of a given radius and returns it"""
    return math.pi * radius * radius

def main():
    """ Launcher """
    radius = int(input("Input the radius of a disk: "))
    print("The area is {}.".format(diskarea(radius)))

if __name__ == "__main__":
    main()