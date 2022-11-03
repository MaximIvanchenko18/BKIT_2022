def field(items, *args):
    assert len(args) > 0
    for dictionary in items:
        res_dict = {}
        for key in args:
            if dictionary.get(key) is not None:
                res_dict[key] = dictionary[key]
        if len(res_dict) == 0:
            pass
        elif len(res_dict) == 1:
            key = [key for key in res_dict.keys()][0]
            yield "'" + str(res_dict[key]) + "'"
        else:
            yield res_dict


def main():
    goods = [
       {'title': 'Ковер', 'price': 2000, 'color': 'green'},
       {'title': 'Диван для отдыха', 'price': 5300, 'color': None}
    ]
    # field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
    # field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
    print(*[elem for elem in field(goods, 'title')], sep=', ')
    print(*[elem for elem in field(goods, 'title', 'price')], sep=', ')
    print(*[elem for elem in field(goods, 'title', 'price', 'color')], sep=', ')


if __name__ == '__main__':
    main()
