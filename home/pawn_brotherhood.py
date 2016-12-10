#!/usr/bin/env python3
"""
http://www.checkio.org/mission/pawn-brotherhood/
"""
import string

LETTERS = string.ascii_lowercase

def safe_pawns(pawns):
	pawn_coords = []
	count=0
	for pair in pawns:
		x = LETTERS.index(pair[0]) + 1
		pawn_coords.append((x,int(pair[1])))

	for row, col in pawn_coords:
		is_safe = (row - 1, col -1) in pawn_coords or (row + 1, col - 1) in pawn_coords
		if is_safe:
			count +=1

	print(count)
	return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
