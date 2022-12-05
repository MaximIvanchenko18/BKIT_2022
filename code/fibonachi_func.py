# Последовательность Фибоначчи
# 0,1,1,2,3,5,8,13,21,34,55,89,144
def fibonachi(n):
    if n <= 0:
        pass
    elif n == 1:
        yield 0
    else:
        yield 0
        yield 1
        prev_2, prev = 0, 1
        for i in range(n-2):
            yield prev_2 + prev
            prev_2, prev = prev, prev_2+prev
