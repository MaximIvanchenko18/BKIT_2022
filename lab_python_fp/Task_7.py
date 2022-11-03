from lab_python_fp.Task_2 import gen_random
from lab_python_fp.Task_3 import Unique
from lab_python_fp.Task_5 import print_result
from lab_python_fp.Task_6 import cm_timer_1
import json
import sys


@print_result
def f1(arg):
    return sorted(Unique([d['job-name'] for d in arg], ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x[:11] == 'программист', arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом python', arg))


@print_result
def f4(arg):
    # return list(zip(arg, list(gen_random(len(arg), 100000, 200000))))
    return [pair[0]+', зарплата '+str(pair[1])+' руб.' for pair in zip(arg, list(gen_random(len(arg), 100000, 200000)))]


def main():
    path = 'data_light.json'
    with open(path, 'r', encoding='UTF8') as f:
        data = json.load(f)
    with cm_timer_1():
        f4(f3(f2(f1(data))))


if __name__ == '__main__':
    main()
