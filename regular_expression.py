from shunting_yard import convert, metachar
from thompsons import run_thompson


def reg_match(infix, string, case_insens=False):
    """ Matching the regular expression and the string.

        Parameters:
            infix (str):The infix expression which is to be convert into postfix and transform into NFA.
            string (str):The string which is to be match against the NFA.
            case_insens (bool):Optional argument which True for case insensitive matching and vice versa.

        Returns:
            nfa.accept_state in cur_state (bool):Returns true if NFA accept state is in the current set of state.
    """
    if case_insens:
        infix = infix.lower()
        string = string.lower()

    # Convert infix into postfix and transform into NFA
    infix = check_concat(infix)
    postfix = convert(infix)
    nfa = run_thompson(postfix)

    cur_states, nxt_states = set(), set()

    # Start the matching by putting the initial state into the current set of states
    cur_states |= current_states(nfa.initial_state)

    for character in string:
        for state in cur_states:
            if state.label == character:
                nxt_states |= current_states(state.edge_1)  # add the edge's state to the next set of states

        cur_states, nxt_states = nxt_states, set()  # set current set of states to the next state of states

    return nfa.accept_state in cur_states  # returns true if there is an accept state at the end of matching


def current_states(state):
    """ Return the set of states that can be reached from state following the edges.

        Parameters:
            state (State):The State object currently pointing to.

        Returns:
            state_set (set<State>):Returns the set of states that is currently in.
    """
    state_set = set()
    state_set.add(state)

    if state.label is None:  # empty state, follow edge and add to set
        if state.edge_1 is not None:
            state_set |= current_states(state.edge_1)
        if state.edge_2 is not None:
            state_set |= current_states(state.edge_2)

    return state_set


def check_concat(infix):
    """ Check if two characters which is not metacharacters are beside each other and add '.' operator between them.

        Parameters:
            infix (State):The infix notation of the expression string.

        Returns:
            new_infix (str):Returns the new infix.
    """
    new_infix = ""
    operators = {**metachar, '(': 60, ')': 60}
    index = 0

    for c in infix:
        if index + 1 != len(infix):  # if c is not last character
            if c not in operators and infix[index + 1] not in operators:  # if both character are not operators
                new_infix += c + '.'
            else:
                new_infix += c
        else:
            new_infix += c

        index += 1

    return new_infix
