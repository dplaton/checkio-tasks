
def checkio(game_result):

    # check the horizontals

    rows = [row for i, row in enumerate(game_result) if len(set(row)) == 1 and row[0] != "."]
    cols = [col for i, col in enumerate(zip(*game_result)) if len(set(col)) == 1 and col[0] != "."]

    diag_1 = [ row[i] for i, row in enumerate(game_result) ]
    diag_2 = [ row[-i-1] for i, row in enumerate(game_result) ]

    value = ""
    for i in [rows,cols]:
        if len(i) > 0:
            value = i[0][0]
            break

    for i in [diag_1, diag_2]:
        if len(set(i)) == 1 and i.count(".") == 0:
            value = i[0][0]
            break

    return value or "D"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"

    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio(["...","XXX","OO."]) == "X"
    assert checkio([".XO","X.X","O.O"]) == "D"
