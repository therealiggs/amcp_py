import my_mdl


print('Enter a line that contains an operand, an operation and a second operation in the mentioned order:')
n1, oper, n2 = input().split()
print(my_mdl.calc(n1, oper, n2))
