""" Solution for https://py.checkio.org/mission/cipher-map2/
"""

def apply_mask(mask, word):
    c = ''
    for i, char in enumerate(word):
        if mask[i] == 'X':
            c = ''.join([c,char])
    return c

def recall_password(cipher_grille, ciphered_password):
    matrix = [list(word) for word in cipher_grille]
    s = ''
    for i in range(0,4):
        for i, word in enumerate(ciphered_password):
            s = ''.join([s, apply_mask(matrix[i], word)])
        matrix = list(zip(*matrix[::-1]))
    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
