def print_result(f):
    def _wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        print(f.__name__)
        if type(res) == list:
            for elem in res:
                print(elem)
        elif type(res) == dict:
            for key, value in res.items():
                print(key, '=', value)
        else:
            print(res)
        return res
    return _wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main():
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == '__main__':
    main()
