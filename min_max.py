
from types import *
from itertools import islice

def min(*args, **kwargs):
    m=None
    key = kwargs.get("key", None)
    if key == None: key = lambda e:e
    # transform everything into a list

    l = []
    for a in args:
        if type(a) == ListType:
            l = a
        elif isinstance(a, str) or type(a) == GeneratorType or isinstance(a,tuple) or isinstance(a, set):
            l = list(a)
        else:
            l = list(islice(args, len(args)))

    print("Min for ", l)
    m = sorted(l, None, key)[0]
    print("Min", m)
    return m

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if key == None: key=lambda e:e

    l = []
    for a in args:
        if type(a) == ListType:
            l = a
        elif type(a) == StringType or type(a) == GeneratorType or type(a) == TupleType:
            l = list(a)
        else:
            l = list(args)

    print("Max for ", l)
    print(sorted(l, None, key))
    m = reduce(lambda x, y: x if key(x) >= key(y) else y, sorted(l, None, key))

    print("Max", m)
    return m

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min(abs(i) for i in range(-10, 10)) == 0, "Abs"
    assert min((9,)) == 9, "Touple"
    assert min({1, 2, 3, 4, -10}) == -10, "Set"
