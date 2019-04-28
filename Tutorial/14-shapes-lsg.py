import math

# to be able to specify type annotations and static type checker mypy
from typing import List, Any, Set, Dict, Tuple, Optional
# importation of abc module for abstract base classes
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    """
    This abstract class defines a abstract method that computes the
    surface of an concrete shape, e.g. circle or rectangle
    """

    @abstractmethod
    def area(self) -> float:
        pass  # no implementation


class Circle(Shape):
    """
    Concrete shape that inherits from abstract class Shape that
    specifies the abstract area() method. area() must be implemented.
    """

    def __init__(self, radius: float) -> None:
        """
        Constructor of the concrete class.
        param radius: the radius of the circle
        """
        self.radius = radius

    def area(self) -> float:
        """
        Computes the area of a disc of a given radius.
        :return: surface of the shape
        """
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, breadth: float) -> None:
        """
        :param width: width of the shape
        :param breath: breath of the shape
        """
        self.width = width
        self.breadth = breadth

    def area(self) -> float:
        """
        :return: surface of the shape
        """
        return self.width * self.breadth


class Square(Rectangle):
    """A Square is in fact a Rectangle with width = breadth"""

    def __init__(self, width: float) -> None:
        """The constructor calls the constructor of the super class Rectangle"""
        super().__init__(width, width)


class Group(Shape):
    """
    A group of shapes is also a shape. Consequently a group can contain
    any king of shapes and other groups. This structure of classes illustrates
    the composite design pattern.
    """

    def __init__(self, shape_list: List[Shape]) -> None:
        """During contruction a list of already created shapes can be provided"""
        self.list = shape_list

    def add(self, shape: Shape) -> None:
        """
        Adds a shape to the collection of the group.
        :param shape: the new shape to add in the group
        """
        self.list.append(shape)

    def area(self) -> float:
        """
        Sums the area of all the shapes contained in the group.
        :return: the sum of the area of every shapes in the group
        """
        area = 0.0
        for shape in self.list:
            area += shape.area()
        return area


def main() -> None:
    """ Launcher """
    c = Circle(10)
    print(c.area())
    r = Rectangle(10, 20)
    print(r.area())
    s = Square(10)
    print(s.area())
    g = Group([r, r, s, c, r])
    print(g.area())
    g.add(r)
    print(g.area())


if __name__ == "__main__":
    main()
