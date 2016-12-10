def checkio(n, m):
    nbin = list(bin(n)[2:].zfill(20))
    mbin = list(bin(m)[2:].zfill(20))
    distance = sum([1 for (x,y) in zip(nbin, mbin) if x != y])
    return distance

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    assert checkio(1, 999999) == 11, "Failed"
