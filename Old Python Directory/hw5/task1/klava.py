from random import randint


def test(prob, testtime, time):  # вероятность в процентах,
    # тесттайм в минутах,
    # время в часах
    flag = False
    for i in range(1, int((time * 60) // testtime + 1)):
        r = randint(1, 100)
        print(r)
        if prob >= r:
            flag = True
    return flag


def sim(number, prob, testtime, time):
    ansline = ''
    count = 0
    for i in range(1, number + 1):
        if test(prob, testtime, time):
            ansline += 'L'
        elif test(prob, 60, 1):  # тест Иннокентия реализован так же,
            # как и Клавин, но с конкретными  значениями
            ansline += 'S'
            count += 1
        else:
            ansline += 'F'
    print(ansline)
    print('Estimated probability of S: {:2.2%}'.format(count / number))


sim(1000, 11, 17, 1.5)
