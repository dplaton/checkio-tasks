
# easiest way out - hardcode all the rules!
LOOKUP = ( (1000, "M"), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40, "XL"), (10,"X"), (9,"IX"), (5,"V"), (1,"I"))

def checkio(data):
    roman = ""
    for num in LOOKUP:
        while data >= num[0]:
            roman += num[1]
            data -= num[0]
            print roman
    return roman

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
