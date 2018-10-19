from memory_profiler import profile
import time


def rotate(lst):
    lst2 = []
    for i in range(len(lst)):
        lst2 += [lst[(i-1) % len(lst)]]
    return lst2


def is_pal(string):
    return string == string[::-1]


def divs(n):
    num = abs(n)
    pdiv = 2
    dividers = [-1, 1]
    if num != 1:
        while pdiv*2 <= num:
            if num % pdiv == 0:
                dividers += [pdiv, pdiv * -1]
            pdiv += 1
        dividers += [num, num * -1]
    return sorted(dividers)


def is_prime(num):
    return len(divs(num)) <= 4


def calc(n1, oper, n2):
    try:
        num1, num2 = int(n1), int(n2)
        if oper == '+':
            return num1 + num2
        elif oper == '-':
            return num1 - num2
        elif oper == '/':
            return num1 / num2
        elif oper == '*':
            return num1 * num2
        else:
            raise RuntimeError("Unknown operation!")
    except ValueError:                           # Возможно, есть лучший способ добавить своё сообщение
        raise ValueError("Wrong operand type!")  # к ошибке, ибо это выглядит не очень оптимально


def pos_divs_sum(num):
    sum = 0
    for i in divs(num):
        if i > 0:
            sum += i
    return sum


def is_perfect(num):
    if type(num) == int and num > 0:
        return num * 2 == pos_divs_sum(num)
    else:
        raise ValueError('Perfection can only be a modifier of a natural number')


@profile
def factor(num):
    err = 'Wrong input format. Factorial is only defined for non-negative integers.'
    if type(num) == int and num > 0:
        ans = 1
        for i in range(1, num+1):
            ans *= i
        return ans
    elif num == 0:
        return 1
    else:
        raise ValueError(err)


@profile
def factor_rec(num):
    err = 'Wrong input format. Factorial is only defined for non-negative integers.'
    if type(num) == int and num > 0:
        return num*factor_rec(num-1)
    elif num == 0:
        return 1
    else:
        return err


def pascal_str(num):
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        return [1] + [(pascal_str(num-1)[i-1] + pascal_str(num-1)[i]) for i in range(1, len(pascal_str(num-1)))] + [1]


def pascal_tri(num):
    if type(num) != int or num < 0:
        raise ValueError('Does it seem funny for you? Please enter something else')
    else:
        ans = []
        for i in range(1, num+1):
            ans += [pascal_str(i)]
        return ans

