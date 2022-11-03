from lab_python_fp import Task_1, Task_2, Task_3, Task_4, Task_5, Task_6, Task_7


def main():
    while True:
        print("Введите номер задания (0 - завершение): ", end='')
        task_number = int(input())
        match task_number:
            case 0:
                break
            case 1:
                Task_1.main()
            case 2:
                Task_2.main()
            case 3:
                Task_3.main()
            case 4:
                Task_4.main()
            case 5:
                Task_5.main()
            case 6:
                Task_6.main()
            case 7:
                Task_7.main()
            case _:
                print("Неверный номер задания!")


if __name__ == '__main__':
    main()
