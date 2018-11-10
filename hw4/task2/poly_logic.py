# Моё авторское решение упорно не хочет дебажиться, поэтому пока что
#  предоставляю решение Ромы Самарина https://gist.github.com/DikiyKazual ,
#  в котором разобрался: мне нужно немного времени, чтобы закончить
# собственное


def proizv(polinom):
    finalpro = ''
    kolvochl = 1
    polinom = list(polinom)
    for i in range(len(polinom)):
        if polinom[i] == ' ':
            polinom[i] = ''
        if polinom[i] == '+' or polinom[i] == '-':
            kolvochl += 1
    copypolinom = ''.join(polinom)
    polinom = ''.join(polinom)
    if polinom.find('x') == -1 and polinom.find('-') == -1 and \
       polinom.find('+') == -1:                 # если одно слагаемое с числом
        return '0'
    if polinom.find('x') != -1 and polinom.find('-') == -1 and \
       polinom.find('+') == -1:                 # если одно слагоемое с иксом
        stroka = polinom
        if stroka.find('x^0') != -1:   # если х в 0 степени
            return '0'
        elif stroka.find('^') == -1:   # если у х нет степени
            if stroka.find('x') == 0:
                return stroka.replace('x', '1')
            if stroka.find('x') != 0:
                return stroka.replace('x', '')
        elif int(stroka[(stroka.find('^') + 1):]) > 1:  # если х в степени > 1
            prosha = stroka[:stroka.find('x')]
            if prosha == '':
                prosha = '1'
            proshb = stroka[(stroka.find('^')+1):]
            buda = str(int(prosha)*int(proshb))
            budb = str(int(proshb) - 1)
            if buda == '0':
                return('0')
            if budb == '1':
                finalpro += buda + 'x'
            else:
                finalpro += buda + 'x^' + budb
        elif stroka.find('x^1') != -1:  # если х в 1 степени
            if stroka.find('x^1') == 0:
                return stroka.replace('x^1', '1')
            if stroka.find('x^1') != 0:
                return stroka.replace('x^1', '')
        return(finalpro)
    for i in range(len(polinom)):
        if copypolinom[i] == '+' or copypolinom[i] == '-':
            znak = copypolinom[i]
            stroka = polinom[:polinom.find(znak)]
            polinom = polinom[polinom.find(znak)+1:]
            if stroka.find('x') == -1:  # если х нет
                finalpro += ''
            elif stroka.find('x^0') != -1:  # если х в 0 степени
                finalpro += ''
            elif stroka.find('^') == -1:   # если у х нет степени
                finalpro += stroka.replace('x', '1')
                finalpro += ' ' + znak + ' '
            elif int(stroka[(stroka.find('^')+1):]) > 1:  # если х в
                prosha = stroka[:stroka.find('x')]        # степени > 1
                if prosha == '':
                    prosha = '1'
                proshb = stroka[(stroka.find('^')+1):]
                buda = str(int(prosha)*int(proshb))
                budb = str(int(proshb) - 1)
                if buda == '0':
                    finalpro += '0'
                elif budb == '1':
                    finalpro += buda + 'x' + ' ' + znak + ' '
                else:
                    finalpro += buda + 'x^' + budb + ' ' + znak + ' '
            elif stroka.find('x^1') != -1 or stroka.find('x^1') != -1:  # если
                                                                # х в 1 степени
                finalpro += stroka.replace('x^1', '1') + ' ' + znak + ' '
    if polinom.find('x') != -1:                 # если последний член с иксом
        finalpro1 = ''
        if polinom.find('x^0') != -1:   # если х в 0 степени
            finalpro1 += '0'
        elif polinom.find('^') == -1:   # если у х нет степени
            if polinom.find('x') == 0:
                finalpro1 += polinom.replace('x', '1')
            if polinom.find('x') != 0:
                finalpro1 += polinom.replace('x', '')
        elif int(polinom[(polinom.find('^')+1):]) > 1:  # если х в степени > 1
            prosha = polinom[:polinom.find('x')]
            if prosha == '':
                prosha = '1'
            proshb = polinom[(polinom.find('^')+1):]
            buda = str(int(prosha)*int(proshb))
            budb = str(int(proshb) - 1)
            if buda == '0':
                return('0')
            if budb == '1':
                finalpro1 += buda + 'x'
            else:
                finalpro1 += buda + 'x^' + budb
        elif polinom.find('x^1') != -1:  # если х в 1 степени
            if polinom.find('x') != 0:
                finalpro1 += polinom.replace('x^1', '')
            else:
                finalpro1 += polinom.replace('x^1', '1')
        finalpro += finalpro1
    if kolvochl > 1 and (finalpro[-3:] == '   ' or
                         finalpro[-3:] == ' + ' or finalpro[-3:] == ' - '):
        finalpro = finalpro[:-3]       # коррекция конца строки
    if kolvochl > 1 and (finalpro[-4:] == ' + 0' or
                         finalpro[-4:] == ' - 0' or finalpro[-3:] == '    '):
        finalpro = finalpro[:-4]
    return(finalpro)
