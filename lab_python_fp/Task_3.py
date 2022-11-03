from lab_python_fp.Task_2 import gen_random


# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.used = set()
        self.items = set(items)
        if len(kwargs) != 0:
            for name, value in kwargs.items():
                if name == 'ignore_case':
                    self.ignore_case = value
        else:
            self.ignore_case = False
        if self.ignore_case is True:
            to_change = set()
            for elem in self.items:
                if isinstance(elem, str):
                    if elem.lower() != elem:
                        to_change.add(elem)
            for elem in to_change:
                self.items.remove(elem)
                self.items.add(elem.lower())

    def __next__(self):
        if len(self.used) == len(self.items):
            raise StopIteration
        for elem in self.items:
            if elem not in self.used:
                self.used.add(elem)
                return elem

    def __iter__(self):
        return self


def iter_print(it):
    while True:
        try:
            print(next(it), end=' ')
        except StopIteration:
            print()
            break


def main():
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    it = Unique(data)
    iter_print(it)

    data = gen_random(10, 1, 3)
    it = Unique(data)
    iter_print(it)

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    it = Unique(data)
    iter_print(it)

    it = Unique(data, ignore_case=True)
    iter_print(it)


if __name__ == '__main__':
    main()
