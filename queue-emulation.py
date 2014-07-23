PUSH_COMMAND = "PUSH"
POP_COMMAND = "POP"

def letter_queue(commands):
    stack = ""

    for c in commands:
        b = c.split()

        if (b[0] == PUSH_COMMAND):
            stack+=b[1]
        else:
            stack = stack[1:] if stack else ''

    return "".join(stack)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
