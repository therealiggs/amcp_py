with open('romantab.txt') as file:  # Находим в интернете табличку
    text = [line for line in file]  # соответсвтвия и переделываем
    # под просто столбец римских чисел

i = 2
nums = [0]
while i <= 3998:
    nums += [text[i][:-1]]
    i += 4

for i in range(1, 1000):
    nums += ['M' + str(nums[i])]

with open('roman.txt', 'w') as file:
    for i in nums:
        print(i, file=file, end='\n')
