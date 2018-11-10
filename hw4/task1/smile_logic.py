def smile(line):
    smiles_left = []
    smiles_right = []
    for i in line:
        if i == '(' or i == '{' or i == '[':
            smiles_left += [i]
        elif i == ')':
            smiles_right += '('
        elif i == '}':
            smiles_right += '{'
        elif i == ']':
            smiles_right += '['
    if len(smiles_left) != len(smiles_right):
        return False
    else:
        i = 0
        while i < len(smiles_left):
            if smiles_left[i] == smiles_right[i]:
                smiles_left.remove(smiles_left[i])
                smiles_right.remove(smiles_right[i])
            i += 1
    return smiles_left[::-1] == smiles_right
