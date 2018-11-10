def poly(line):
    ans = ''
    start = 0
    end = min(line.find('-'), line.find('+'))
    if end == -1:
        end = max(line.find('-'), line.find('+'))
    while end != -1:
        ans += str(int(line[start:line.find('x', start)]) * int(line[line.find('^', start) + 1:end])) + 'x^' + \
               str(int(line[line.find('^', start) + 1:end]) - 1)
        start = end + 1
        end = min(line.find('-', start), line.find('+', start))
        if end == -1:
            end = max(line.find('-', start), line.find('+'), start)
    ans += str(int(line[:line.find('x')]) * int(line[line.find('^')+1:len(line)])) + 'x^' + str(int(line[line.find('^') + 1:len(line)]) - 1)
    return ans


print(poly('20x^30+20x^30'))
