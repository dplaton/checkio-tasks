""" Solution for https://py.checkio.org/mission/friendly-number
"""
from decimal import Decimal

def friendly_number(number, base=1000, decimals=0,
                    suffix='', powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    # cut the base and determine the index in one go
    power_index = 0
    while abs(number) >= base and power_index < len(powers)-1:
        number = Decimal(number) / Decimal(base)
        power_index += 1

    power = powers[power_index]

    # round the number ourselves since the default
    # rounding is not towards zero
    if decimals == 0:
        number = int(float(number)/1)

    template = "{:.{d}f}{p}{s}"
    final = template.format(number, d=decimals, p=power, s=suffix)
    return final

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(-150, base=100, powers=["", "d", "D"]) == '-1d'
    assert friendly_number(255000000000, powers=["", "k", "M"]) == '255000M'
    assert friendly_number(10**24) == "1Y"
    assert friendly_number(10**32) == "100000000Y"

