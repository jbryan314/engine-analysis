from src.model.ports.port import Port
import unittest


class Base(unittest.TestCase):
    """
    Base class for tests. This class includes a setUp method for defining attributes for a tests and a tearDown method
    for cleaning up a class instance after a test.
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass


class Instantiation(Base):
    """
    Tests all aspects of instantiation, including instantiating with args of wrong type, instantiation of input values
    outside of constraints, etc.
    """
    # Input arguments wrong type
    # ==========================
    # Input arguments outside constraints
    # ===================================


class Set(Base):
    """
    Tests all aspects of setting attributes, including setting attributes of wrong type, setting attributes outside
    their constraints, etc
    """
    # Set attribute wrong type
    # ========================
    # Set attribute outside constraints
    # =================================
    pass


class MethodsInput(Base):
    """
    Tests methods which take inputs for passing invalid inputs, etc.
    """
    # Invalid input type
    # ==================
    # Invalid input value
    # ====================
    pass


class MethodsReturnType(Base):
    """
    Tests methods' return types
    """
    pass


class MethodsReturnValues(Base):
    """
    Tests methods' return values against known values
    """
    pass


if __name__ == '__main__':
    unittest.main()
