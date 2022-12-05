import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_single_arg(self):
        """
        Check strings return for single arg
        """
        goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'}, {'title': 'Диван для отдыха', 'price': 5300,
                                                                       'color': 'black'}]
        self.assertEqual([elem for elem in field(goods, 'title')], ["'Ковер'", "'Диван для отдыха'"])

    def test_some_args(self):
        """
        Check dictionary return for some args
        """
        goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'}, {'title': 'Диван для отдыха', 'price': 5300,
                                                                       'color': 'black'}]
        self.assertEqual([elem for elem in field(goods, 'title', 'price', 'color')], [{'title': 'Ковер',
        'price': 2000, 'color': 'green'}, {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}])

    def test_with_None_fields(self):
        """
        CHeck absence of None field
        """
        goods = [
            {'title': 'Ковер', 'price': None, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': None}
        ]
        self.assertEqual([elem for elem in field(goods, 'title', 'price', 'color')], [{'title': 'Ковер',
        'color': 'green'}, {'title': 'Диван для отдыха', 'price': 5300}])

    def test_all_None(self):
        """
        Check return nothing when all fields are None
        """
        goods = [{'title': None, 'price': None}, {'title': None, 'price': None}]
        self.assertEqual([elem for elem in field(goods, 'title', 'price')], [])


if __name__ == '__main__':
    unittest.main()
