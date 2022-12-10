import unittest
from data_connections import *
from task_1 import house_num_more_3
from task_2 import streets_with_min_resident_cnt
from task_3 import data_sorted_by_house_num


class MyTestCase(unittest.TestCase):
    def test_task_1(self):
        res = [(5, 2, 100, 'Веселая'), (10, 3, 232, 'Замечательная'), (7, 1, 260, 'Великолепная'), (4, 1, 170,
                                                                                                    'Великолепная')]
        self.assertEqual(house_num_more_3(one_to_many), res)

    def test_task_2(self):
        res = [('Великолепная', 170), ('Замечательная', 125), ('Веселая', 100)]
        self.assertEqual(streets_with_min_resident_cnt(one_to_many), res)

    def test_task_3(self):
        res = [(2, 1, 125, 'Замечательная'), (2, 1, 125, 'Неповторимая (старое название)'), (3, 4, 200, 'Великолепная'),
               (3, 4, 200, 'Отличная (старое название)'), (4, 1, 170, 'Великолепная'), (4, 1, 170,
               'Отличная (старое название)'), (5, 2, 100, 'Веселая'), (5, 2, 100, 'Потрясная (старое название)'), (7, 1,
               260, 'Великолепная'), (7, 1, 260, 'Отличная (старое название)'), (10, 3, 232, 'Замечательная'), (10, 3,
               232, 'Неповторимая (старое название)')]
        self.assertEqual(data_sorted_by_house_num(many_to_many), res)


if __name__ == '__main__':
    unittest.main()
