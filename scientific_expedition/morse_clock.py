# http://www.checkio.org/mission/morse-clock/


def checkio(time_string):
    """ Split the time_string into time components, then convert each digit
    to binary. At the end, translate everything using maketrans. Lots of
    formatting on the way
    """
    be = []
    for el in time_string.split(":"):
        be.extend([str(bin(int(d)))[2:] for d in el.zfill(2)])

    bc = "{:0>2s} {:0>4s} : {:0>3s} {:0>4s} : {:0>3s} {:0>4s}".format(
        *be)
    return bc.translate(str.maketrans({"0": ".", "1": "-"}))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(
        "21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(
        "23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
