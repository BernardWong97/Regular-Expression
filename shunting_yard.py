# Bernard Wong
# Shunting Yard Algorithm


def convert(infix):
    """ Uses Shunting Yard Algorithm to convert infix expression to postfix expression.

        Parameters:
            infix (str):The infix expression which is to be convert to postfix.

        Returns:
            postfix (str):The postfix expression which was converted from infix.

    """
    # The metacharacters that defines the operation of the regular expression.
    # * : 0 or more
    # . : concatenate
    # | : one or the other
    metachar = {'*': 50, '+': 50, '.': 40, '|': 30}  # value represents the precedence level

    stack = []
    postfix = ""

    for c in infix:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':  # pop from stack and add to postfix until open bracket
                postfix += stack.pop()
            stack.pop()  # pop the open bracket off the stack
        elif c in metachar:
            # if c's precedence is equal smaller than the value of the last element of the stack, pop and add to postfix
            while stack and metachar.get(c, 0) <= metachar.get(stack[-1], 0):
                postfix += stack.pop()
            stack.append(c)
        else:
            postfix += c

    while stack:  # pop and everything on stack to postfix
        postfix += stack.pop()

    return postfix
