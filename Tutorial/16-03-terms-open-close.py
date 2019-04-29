# to be able to specify type annotations and static type checker mypy
from typing import List, Any, Set, Dict, Tuple, Optional
# importation of abc module for abstract base classes
from abc import ABCMeta, abstractmethod
# for enum support
from enum import Enum, unique

"""
This version makes use of delegation to compute the result of each operator by 
defining a new sub-class of Bin_op or Una_op.
This version conforms the Open-Close-Principle.
"""


class EmptyException(Exception):
    """Empty string exception, raised whenever an empty string is not expected"""

    def __init__(self, message):
        self.message = message


class NotBoundException(Exception):
    """Variable without binding exception, raised whenever a variable is not bound with a value"""

    def __init__(self, message):
        self.message = message


class Context:
    """
    Stores the values assigned to the variables into a lookup table (a dictionary).
    Each entry of the lookup table is a pair (name of variable, value)
    Some methods allows us to bind a value to a named variable,
    to change the assignement and to evaluate a variable.
    """

    def __init__(self) -> None:
        "Just create an empty dictionary"
        self.lookup_table: Dict[str, float] = {}

    def bind(self, name: str, value: float) -> None:
        """
        If the variable, called name, does not exists in the dictionary
        lookup_table then a new assigment is added into the dictionary otherwise
        the value of the variable is changed.
        :param name: name of the variable
        :param value: value to assign to the variable
        """
        if not name:  # is name empty
            raise EmptyException("The variable's name is empty in bind()")
        self.lookup_table[name] = value  # create entry and/or change value

    def get_value(self, name: str) -> float:
        if not name:  # name is empty
            raise EmptyException("The variable's name is empty in get_value()")
        if name in self.lookup_table:
            return self.lookup_table[name]
        else:
            raise NotBoundException("The variable '" + name + "' is not bound to a value")


class Bin_op(metaclass=ABCMeta):
    """Abstract class that represents a binary operator and the implementation of its computation"""

    def compute(x: float, y: float) -> float:
        """
        Implementation of the binary operation.
        :param x: left operand
        :param y: right operand
        :return: the result of the operation
        """
        pass


class Add(Bin_op):
    def compute(x: float, y: float) -> float:
        return x + y


class Sub(Bin_op):
    def compute(x: float, y: float) -> float:
        return x - y


class Mul(Bin_op):
    def compute(x: float, y: float) -> float:
        return x * y


class Div(Bin_op):
    def compute(x: float, y: float) -> float:
        return x / y


class Una_op(metaclass=ABCMeta):
    """Abstract class that represents a unary operator and the implementation of its computation"""

    def compute(x: float) -> float:
        """
        Implementation of the unary operation.
        :param x: single operand
        :return: the result of the operation
        """
        pass


class Neg(Una_op):
    def compute(x: float) -> float:
        return (-1) * x


"""
Adding a new operation consists simply to add a new class 
without any changes of existing classes
"""


class Abs(Una_op):
    def compute(x: float) -> float:
        return -x if x < 0 else x


class Term(metaclass=ABCMeta):
    """
    This abstract class defines a abstract method that evaluates
    a term (expression)
    """

    @abstractmethod
    def eval(self, context: Context) -> float:
        """
        Abstract method that evaluate a term.
        :param context: where the bindings (variable name, value) are stored
        :return: the value of the evaluated term
        """
        pass  # no implementation


class Constant(Term):
    """
    The value of a constant cannot (obviously) change.
    The value is initialized during the creation.
    """

    def __init__(self, value: float) -> None:
        """
        Defines the constant value.
        :param value: the constant value to initialize
        """
        self.value = value

    def eval(self, context: Context) -> float:
        """
        :param context: where the bindings are located (not use for constants)
        :return: simply the value
        """
        return self.value


class Variable(Term):
    """
    The value of a variable can be modified via the context object.
    """

    def __init__(self, name: str) -> None:
        """
        A variable is created and added to the context
        :param name: name of the variable
        :param value: value of the variable
        """
        if not name:  # is name is empty
            raise EmptyException("The variable's name cannot be empty in Variable")
        self.name = name

    def eval(self, context: Context) -> float:
        """
        :param context: dictionnary of bindings, this object is not stored as an attribute
        :return: the value of the variable
        """
        return context.get_value(self.name)


class Binary_expression(Term):
    """
    A binary expression has two terms (left, right) and a binary operator.
    """

    def __init__(self, left: Term, right: Term, bin_op: Bin_op) -> None:
        """
        :param left: left term
        :param right: right term
        :param bin_op: binary operator
        """
        self.left = left
        self.right = right
        self.bin_op = bin_op

    def eval(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :param context: where the bindings are located
        :return: the evaluated value of the binary expression
        """
        value_left = self.left.eval(context)
        value_right = self.right.eval(context)
        return self.bin_op.compute(value_left, value_right)


class Unary_expression(Term):
    """
    A unary expression has on term and a unary operator.
    """

    def __init__(self, term: Term, una_op: Una_op) -> None:
        """
        :param term: single term
        :param una_op: binary operator
        """
        self.term = term
        self.una_op = una_op

    def eval(self, context: Context) -> float:
        """
        Evaluates both the terms first and then apply the binary_operator
        :param context: where the bindings are located
        :return: the evaluated value of the binary expression
        """
        value_term = self.term.eval(context)
        return self.una_op.compute(value_term)


def main() -> None:
    """ Launcher """
    ctx = Context()
    three = Constant(3)
    five = Constant(5)
    print("Constant 3: ", three.eval(ctx))
    print("Constant 5: ", five.eval(ctx))
    v = Variable("d")
    ctx.bind("d", 7)  # define d = 7
    try:
        print("Variable d: ", v.eval(ctx))
    except EmptyException as empty:
        print(empty.message)
    except NotBoundException as notbound:
        print(notbound.message)

    neg = Unary_expression(v, Neg)
    print("-d: ", neg.eval(ctx))

    neg_value = Constant(-23)
    absol = Unary_expression(neg_value, Abs)
    print("abs(-23): ", absol.eval(ctx))

    addition = Binary_expression(three, neg, Add)
    print("3 + (-d): ", addition.eval(ctx))
    multiplication = Binary_expression(addition, five, Mul)
    print("(3 + -d) * 5: ", multiplication.eval(ctx))

    try:
        v2 = Variable("v2")
        print("Variable v2: ", v2.eval(ctx))
    except (EmptyException, NotBoundException) as error:
        print(error.message)

    try:
        v3 = Variable("")
        print("Variable v3: ", v3.eval(ctx))
    except (EmptyException, NotBoundException) as error:
        print(error.message)


if __name__ == "__main__":
    main()
