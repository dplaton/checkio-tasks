"""You are given an expression with numbers, brackets and operators. For this task only the brackets matter. 
Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, 
then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. 
For this task, you should to make a decision to correct an expression or not based on the brackets. Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).
Output: A verdict on the correctness of the expression in boolean (True or False).

Precondition: 
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 10^3
"""
OPEN_BRACKETS = ("{","[","(")
CLOSE_BRACKETS = ("}","]",")")

def checkio(expression):

    # let's have a stack of "open brackets"
    stack = []

    # parse the expression, extract the brackets
    for ch in expression:
        if ch in OPEN_BRACKETS:
            # open bracket goes into the stack
            stack.append(OPEN_BRACKETS[OPEN_BRACKETS.index(ch)])

        if ch in CLOSE_BRACKETS:
            # if stack is empty it means we have an orphan closing bracket
            if len(stack) == 0:
                return False
            # closed bracket it compared to the top of the stack
            if stack.pop() != OPEN_BRACKETS[CLOSE_BRACKETS.index(ch)]:
                # this means we didn't close them in order
                return False

    # if there's anything left in the stack it means that we have orphan brackets
    return len(stack) == 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
