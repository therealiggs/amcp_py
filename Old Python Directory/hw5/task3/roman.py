with open('roman.txt') as file:
    text = [line[:-1] for line in file]


class Roman:

    def __init__(self, number):
        if 2000 > number > 0:
            self.name = 'Roman'
            self.arabic = number
        else:
            raise ValueError('Only [1,1999] interval allowed')

    def __str__(self):
        return text[self.arabic]

    def __add__(self, other):
        try:
            return Roman(self.arabic + other.arabic)

        except AttributeError:
            raise TypeError('You seem to be tryna add smth'
                            ' wrong to my lovely roman number')

    def __eq__(self, other):
        try:
            return self.arabic == other.arabic

        except AttributeError:
            raise TypeError('You seem to be tryna compare smth'
                            ' wrong to my lovely roman number')

    def __int__(self):
        return self.arabic
