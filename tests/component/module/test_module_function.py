import unittest
from unittest.mock import Mock
from run.module.module_function import module

class module_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.module_class = Mock()

    def test(self):
        result = module(self.module_class)
        self.assertEqual(result, self.module_class.return_value)
        # Check class call
        self.module_class.assert_called_with()

    def test_with_kwargs(self):
        result = module(**self.kwargs)(self.module_class)
        self.assertEqual(result, self.module_class.return_value)
        # Check class call
        self.module_class.assert_called_with(**self.kwargs)