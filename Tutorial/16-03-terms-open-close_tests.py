import unittest
from terms_open_close import *


class Test_context(unittest.TestCase):

    def test_bind_get_value(self):
        """Checks that binding an identifier with a value and get_value return the same value"""
        identifier = "v"
        value = 10.5
        a_var = Variable(identifier)
        ctx = Context()
        ctx.bind(identifier, value)
        self.assertEqual(ctx.get_value(identifier), value)

    def test_bind_empty(self):
        """Checks that binding an empty identifier raises an exception"""
        identifier = ""
        ctx = Context()
        value = 0.0
        with self.assertRaises(EmptyException):
            ctx.bind(identifier, value)

    def test_get_value_empty(self):
        """Checks that getting a value for an empty identifier raises an exception"""
        identifier = ""
        ctx = Context()
        with self.assertRaises(EmptyException):
            ctx.get_value(identifier)


class Test_constant(unittest.TestCase):

    def test_eval(self):
        """Checks the evaluation of a constant works fine"""
        value = 4.03
        four = Constant(value)
        ctx = Context()
        self.assertEqual(Constant.eval(four, ctx), value)


class Test_variable(unittest.TestCase):

    def test_eval(self):
        """Checks that the evaluation of a variable works fine"""
        identifier = "v"
        value = 10.5
        a_var = Variable(identifier)
        ctx = Context()
        ctx.bind(identifier, value)
        self.assertEqual(a_var.eval(ctx), value)

    def test_creation_empty(self):
        """Checks that the creation of an empty variable raises an exception"""
        emtpy_identifier = ""
        with self.assertRaises(EmptyException):
            a_var = Variable(emtpy_identifier)


class Test_binary_expression(unittest.TestCase):

    def test_eval(self):
        """Checks that the evaluation of a binary expression works fine for each operator"""
        value = 5.0
        term = Constant(value)
        ctx = Context()
        bin_expr = Binary_expression(term, term, Add)
        self.assertEqual(bin_expr.eval(ctx), value + value)
        bin_expr = Binary_expression(term, term, Sub)
        self.assertEqual(bin_expr.eval(ctx), value - value)
        bin_expr = Binary_expression(term, term, Mul)
        self.assertEqual(bin_expr.eval(ctx), value * value)
        value2 = 2.0
        term_right = Constant(value2)
        bin_expr = Binary_expression(term, term_right, Div)
        self.assertEqual(bin_expr.eval(ctx), value / value2)

    def test_div_0(self):
        """Checks that the division by 0 raises an exception"""
        ctx = Context()
        bin_expr = Binary_expression(Constant(27), Constant(0), Div)
        with self.assertRaises(ZeroDivisionError):
            bin_expr.eval(ctx)


class Test_unary_expression(unittest.TestCase):

    def test_eval_neg(self):
        """Checks that the evaluation of a unary expression works fine"""
        value = 5.0
        term = Constant(value)
        ctx = Context()
        una_expr = Unary_expression(term, Neg)
        self.assertEqual(una_expr.eval(ctx), (-1) * value)

    def test_eval_abs(self):
        """Checks that the evaluation of a unary expression works fine"""
        value = -15.0
        term = Constant(value)
        ctx = Context()
        una_expr = Unary_expression(term, Abs)
        self.assertEqual(una_expr.eval(ctx), abs(value))



