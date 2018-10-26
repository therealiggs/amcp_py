with open('caesar.txt') as file:    # Задачу, аналогичную той, что задана в третьем дз, я уже решал в немного
    text = [line for line in file]  # усложнённом варианте. Это отформатированный код, залитый мной на гитхаб
    # в репозиторий oldpystuff 14го июня 2017 года. Конечно, это не тот формат, в котором Вы просили сдать дз, но, может
    # быть, бывают и исключения? ^_^ Просто ооооочень лень переписывать интерфейс и тесты...


def code(word, key):
    ans = []
    for line in word:
        e = line.encode('cp1251')
        s = bytes([(byte + key) % 256 for byte in e])
        ans += s.decode('cp1251')
    return ''.join(i for i in ans)


def decode(word, key):
    ans = []
    for line in word:
        e = line.encode('cp1251')
        s = bytes([(byte - key) % 256 for byte in e])
        ans += s.decode('cp1251')
    return ''.join(i for i in ans)


print('Ключ?')
gkey = int(input())

with open('caesar.txt', 'w') as file:
    flag = False
    while not flag:
        print('Что делать?')
        command = input()
        if 'зашифровать'.startswith(command.lower()):
            for char in code(text, gkey):
                print(char, file=file, end='')
            flag = True
        elif 'расшифровать'.startswith(command.lower()):
            for char in decode(text, gkey):
                print(char, file=file, end='')
            flag = True
        else:
            print('Нет такой команды!')
