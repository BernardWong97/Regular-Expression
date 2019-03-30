# Bernard Wong
# Thompson's Construction Algorithm


class State:
    """ State object represents a state with a label and two edges in a NFA.

        Attributes:
            label (str):A label which representing the State object.
            edge_1 (State):A pointer to another State object representing an edge.
            edge_2 (State):A pointer to another State object representing a second edge.
    """
    label = None
    edge_1 = None
    edge_2 = None


class NFA:
    """ Represents a Non-deterministic finite automaton.

        Attributes:
            initial_state (State):Represents the initial State of the NFA.
            accept_state (State):Represents the accept State of the NFA.
    """
    initial_state = None
    accept_state = None

    def __init__(self, initial_state, accept_state):
        self.initial_state = initial_state
        self.accept_state = accept_state


def run_thompson(postfix):
    """ Transform postfix expression into NFA.

        Parameters:
            postfix (str):The postfix expression which is to be transform into NFA.

        Returns:
            a NFA object (NFA):The NFA that was transformed from the postfix expression.
    """
    nfa_stack = []

    for c in postfix:
        if c == '.':
            # pop two nfa from stack (the order is important)
            nfa_2, nfa_1 = nfa_stack.pop(), nfa_stack.pop()
            # create a new bigger nfa by combining both nfa and push back into the stack
            nfa_1.accept_state.edge_1 = nfa_2.initial_state
            nfa_stack.append(NFA(nfa_1.initial_state, nfa_2.accept_state))
        elif c == '|':
            # pop two nfa from stack
            nfa_2, nfa_1 = nfa_stack.pop(), nfa_stack.pop()
            # create a new initial state and connect to both of the nfa's initial stack
            new_initial_state = State()
            new_initial_state.edge_1, new_initial_state.edge_2 = nfa_1.initial_state, nfa_2.initial_state
            # create a new accept state and connect both of the nfa's accept state to it
            new_accept_state = State()
            nfa_1.accept_state.edge_1, nfa_2.accept_state.edge_1 = new_accept_state, new_accept_state
            # push back the new bigger nfa to the stack
            nfa_stack.append(NFA(new_initial_state, new_accept_state))
        elif c == '*':
            # pop one nfa from stack
            nfa = nfa_stack.pop()
            # create a new initial and accept states
            new_initial_state, new_accept_state = State(), State()
            # connect new initial state to the nfa's initial state and new accept state
            new_initial_state.edge_1,  new_initial_state.edge_2 = nfa.initial_state, new_accept_state
            # connect nfa's accept state to new accept state and nfa's initial_state
            nfa.accept_state.edge_1,  nfa.accept_state.edge_2 = new_accept_state, nfa.initial_state
            # push back the new bigger nfa to the stack
            nfa_stack.append(NFA(new_initial_state, new_accept_state))
        elif c == '+':
            # pop one nfa from stack
            nfa = nfa_stack.pop()
            # create a new initial and accept states
            new_initial_state, new_accept_state = State(), State()
            # connect new initial state to the nfa's initial state
            new_initial_state.edge_1 = nfa.initial_state
            # connect nfa's accept state to new accept state and nfa's initial_state
            nfa.accept_state.edge_1, nfa.accept_state.edge_2 = new_accept_state, nfa.initial_state
            # push back the new bigger nfa to the stack
            nfa_stack.append(NFA(new_initial_state, new_accept_state))
        elif c == '?':
            # pop one nfa from stack
            nfa = nfa_stack.pop()
            # create a new initial and accept states
            new_initial_state, new_accept_state = State(), State()
            # connect new initial state to the nfa's initial state and new accept state
            new_initial_state.edge_1,  new_initial_state.edge_2 = nfa.initial_state, new_accept_state
            # connect nfa's accept state to new accept state
            nfa.accept_state.edge_1 = new_accept_state
            # push back the new bigger nfa to the stack
            nfa_stack.append(NFA(new_initial_state, new_accept_state))
        else:
            # if c is normal character, create a NFA and push to stack
            initial_state, accept_state = State(), State()

            initial_state.label,  initial_state.edge_1 = c, accept_state

            nfa_stack.append(NFA(initial_state, accept_state))

    # should only contains 1 nfa and return it
    return nfa_stack.pop()
