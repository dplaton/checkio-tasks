from math import sqrt, floor
from operator import mul

def checkio(number):
    print "Checking ", number
    if 0 <= number <= 9:
        return number

    #prime factorization of N
    primes = deconstruct_number(number)

    # eliminate primes > 10
    # because we only need digits
    temp = [ x for x in primes if x < 10 ]
    primes = temp

    l = len(primes)
    # if no primes or just one prime number then return 0
    if l <= 1:
        return 0

    # the initial minimum
    if reduce(mul, primes, 1) != number:
        return 0
    min = int("".join(map(str, primes)))
    print "Initial minimum is ", min
    # if we only have to primes in the array then
    # the minimum is the number we're looking for
    if l == 2:
        return min
    cnt = 0
    while True and cnt < 10:
        # build a new list
        primes = shorten_list(primes)
        if len(primes) == l:
            break
        print "Iteration ", cnt, primes

        # check the joined digits
        n = int("".join(map(str,sorted(primes))))

        if min > n:
            print "New minimum", n
            min = n


        # if there's just two digits left - that's our minimum
        if len(primes) == 2:
            break

        cnt += 1
    print "Returning ", min
    return min

def shorten_list(l):
    print "Reducing ", l
    done = False
    for i in range(0, len(l)):
        j = 1
        while j < len(l) and not done:
            prod = l[i]*l[j]
            if prod < 10:
                l[i] = prod
                del l[j]
                done = True
            j+=1
    return sorted(l)



def deconstruct_number(n):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return q <= maxq and [q] + deconstruct_number(n//q) or [n]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(560) == 2578
    assert checkio(3247) == 0
    assert checkio(124) == 0
    assert checkio(1680) == 5678
