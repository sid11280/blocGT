def result(circuit):
    a = False
    b = False
    a_defined = False
    b_defined = False
    out = [False,  False, False]
    for j in range(0, len(circuit[0])):
        for i in range(0, len(circuit)):
            val = circuit[i][j]
            if val == '1' or val == '0':
                if b_defined:
                    return None
                if a_defined:
                    b = (val == '1')
                    b_defined = True
                    out[2] = b
                else:
                    a = (val == '1')
                    a_defined = True
                    out[0] = a
            elif val == 'NOT':
                if i == 1 and not b_defined:
                    return None
                out[i] = not out[i]
            elif val == 'AND':
                if i != 1:
                    return None
                out[1] = out[0] and out[2]
            elif val == 'OR':
                if i != 1:
                    return None
                out[1] = out[0] or out[2]
            elif val == 'OUT':
                return out[i]
    return None

