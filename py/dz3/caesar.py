from caesar_logic import encrypt, decrypt

print('What do we do?')
call = input()
if call == 'e':
    print('Enter the phrase')
    text = input()
    print('Enter the key')
    key = int(input())
    print(encrypt(key, text))
elif call == 'd':
    print('Enter the phrase')
    text = input()
    print('Enter the key')
    key = int(input())
    print(decrypt(key, text))
else:
    print('Unknown call')
