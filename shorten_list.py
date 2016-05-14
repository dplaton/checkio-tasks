def shorten_list(l):
    print "Reducing ", l
    temp = []
    done = False
    for i in range(0, len(l)):
        j = 1
        while j < len(l) and not done:
            prod = l[i]*l[j]
            if prod < 10:
                l[i] = prod
                del l[j]
                done = True

    return sorted(l)


assert shorten_list([2,3,4,5]) == [4,5,6]
assert shorten_list([2,2,5]) == [4, 5]
