import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Флаг для определения момента, когда считаем число
    got_it = False
    while not got_it:
        try:
            # Пробуем преобразовать в действительное число
            coef = float(coef_str)
            got_it = True
        except:
            print(prompt)
            coef_str = input()
            continue
    return coef


def get_bi_roots(sq_root):
    res = []
    if sq_root == 0:
        res.append(0)
    elif sq_root > 0:
        bi_root = math.sqrt(sq_root)
        res.append(bi_root)
        res.append(-bi_root)
    return res

def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        sq_root = -b / (2.0 * a)
        result.extend(get_bi_roots(sq_root))
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.extend(get_bi_roots(root1))
        result.extend(get_bi_roots(root2))
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {:.5f} и {:.5f}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {:.5f} и {:.5f} и {:.5f}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {:.5f} и {:.5f} и {:.5f} и {:.5f}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4