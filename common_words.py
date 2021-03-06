""" Solution for https://checkio.org/mission/common-words/

Lambda fun:
    The & operator is the "intersection" operator for sets. The rest is easy as pie"""

checkio = lambda first,second:",".join(sorted([s for s in set(first.split(",")) & set(second.split(","))]))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"
