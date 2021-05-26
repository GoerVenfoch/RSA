import sympy

def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - y * (a // b)

def generate_keys():
    minValue = 10**28
    maxValue = 10**29
    arr_keys = []
    p = sympy.randprime(minValue, maxValue)
    q = sympy.randprime(minValue, maxValue)
    n = str(p * q)
    if len(n) < 58:
        return generate_keys()
    d = (p-1)*(q-1)
    s = sympy.randprime(3, 1000)
    gcdexVal, _, _ = gcdex(s, d)
    while gcdexVal != 1:
        s = sympy.randprime(3, 1000)
        gcdexVal, _, _ = gcdex(s, d)
    _, e, _ = gcdex(s, d)
    arr_keys.append(int(n))
    arr_keys.append(s)
    arr_keys.append(e)
    return arr_keys

def create_char_table():
    tableSymbols = {letter: charCode + 1000 for charCode, letter in enumerate('.,?!;:-()""`\'\n []{}№@#$&%*+=><|~/')}
    for charCode, letter in enumerate('0123456789'):
        tableSymbols[letter] = charCode + 1033
    for num, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
        tableSymbols[letter] = num + 1043
    for num, letter in enumerate('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'):
        tableSymbols[letter] = num + 1069
    return tableSymbols

        
