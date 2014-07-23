PUSH_COMMAND = "PUSH"
POP_COMMAND = "POP"
PEEK_COMMAND = "PEEK"

def digit_stack(commands):
    stack = []
    s = 0
    for c in commands:
        if PUSH_COMMAND in c.upper():
            stack.append(int(c.strip()[-1]))
        elif PEEK_COMMAND in c and stack:
            s += stack[-1]
        elif POP_COMMAND in c and stack:
            s += stack.pop()

    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
