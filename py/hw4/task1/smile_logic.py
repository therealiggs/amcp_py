def smile(line):
    stack = []
    flag = True
    for i in line:
        if i == '(' or i == '{' or i == '[':
            stack += [i]
        elif (i == ')' or i == '}' or i == ']') and len(stack) == 0:
            flag = False
        elif stack:
            if not (not (i == ')' and stack[-1] == '(') and
                    not (i == '}' and stack[-1] == '{') and
                    not (i == ']' and stack[-1] == '[')):
                stack.pop()
    return stack == [] and flag
