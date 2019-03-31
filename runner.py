from regular_expression import reg_match


def main():
    print("=== Welcome To Regular Expression String Matching Program ===")
    print("""This program supports 5 regular expression's metacharacters:
    * : 0 or more
    + : 1 or more
    ? : 0 or 1
    . : concatenate
    | : one or the other""")
    cont = True

    while cont:
        infix = input("Please input regular expression in infix notation:\n")
        string = input("Please input a string for matching:\n")
        case_sens = input_validation("Do you want case sensitive matching? (Y/N)\n")

        if case_sens == 'Y':
            print("Result of matching \"%s\" and \"%s\" = \"%s\"" % (infix, string, reg_match(infix, string, False)))
        else:
            print("Result of matching \"%s\" and \"%s\" = \"%s\"" % (infix, string, reg_match(infix, string, True)))

        new_matching = input_validation("New matching? (Y/N)\n")

        if new_matching == 'Y':
            continue
        else:
            cont = False

    print("Thank you for using Regular Expression String Matching Program!\n=== Bye Bye! ===")


def input_validation(message):
    """ Validate the input Y or N only.

        Parameters:
            message (str):The message to ask user what to input.

        Returns:
            user_input (str):Returns Y or N.
    """
    user_input = input(message)
    user_input = user_input.upper()

    while user_input not in ('Y', 'N'):
        print("Please enter Y or N only.")
        user_input = input(message)
        user_input = user_input.upper()

    return user_input


if __name__ == "__main__":
    main()
