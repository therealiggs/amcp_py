def rotate(lst):
    lst2 = []
    for i in range(len(lst)):
        lst2 += [lst[(i-1) % len(lst)]]
    return lst2


def is_pal(string):
    return string == string[::-1]


def divs(num):
    pdiv = 2
    dividers = [1]
    if num != 1:
        while pdiv*2 <= num:
            if num % pdiv == 0:
                dividers += [pdiv]
            pdiv += 1
        dividers += [num]
    return dividers


def is_prime(num):
    return len(divs(num)) <= 2


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






