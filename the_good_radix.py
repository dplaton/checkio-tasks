"""
https://checkio.org/mission/good-radix/
"""
import string
all_chars = string.digits + string.ascii_uppercase

def checkio(number):
    """
    Your solution
    """
    min_radix = all_chars.index(max(number).upper())

    return min(filter(lambda k:int(number, k) % (k-1) == 0, range(min_radix+1, len(all_chars) + 1)) or [0])
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"18") == 10, "Simple decimal"
    assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    assert checkio(u"222") == 3, "3rd test"
    assert checkio(u"A23B") == 14, "It's not a hex"
    assert checkio(u"IDDQD") == 0, "k is not exist"
    assert checkio(u"ZZZ") == 36, "Last radix"
    print('Local tests done')
