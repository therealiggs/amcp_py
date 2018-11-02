def encrypt(offset, text):
    if type(offset) != int or type(text) != str:
        raise ValueError('Wrong input format')
    ans = ''
    alph = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    true_offset = offset % len(alph)
    for i in text:
        if i == ' ':
            ans += i
        else:
            if ord(i) < 65 or 97 > ord(i) > 90 or ord(i) > 122:
                raise ValueError('Current alphabet doesn\'t have that symbol')
            if alph.index(i) + true_offset > 51:
                true_offset -= 52
            ans += alph[alph.index(i) + true_offset]
    return ans


def decrypt(offset, text):
    return encrypt(offset * -1, text)
