#!/usr/bin/env python3
"""
http://www.checkio.org/mission/feed-pigeons
Not submitted
"""
def checkio(portions):
	initial = portions
	pigeons_fed = 0
	minute=0
	pigeons = 0
	old_pigeons = 0
	cnt = 0
	while True:
		minute += 1
		old_pigeons = pigeons
		pigeons += minute

		if portions < pigeons:
			remaining_portions = portions - old_pigeons
			if remaining_portions > 0:
				pigeons_fed += remaining_portions
			break
		else:
			portions -= pigeons
			pigeons_fed += minute
	return pigeons_fed

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"

    for i in range(1,20):
    	checkio(i)
