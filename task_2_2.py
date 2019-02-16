import argparse

class NFA:
    def __init__(self, initial_state, final_state, states, transitions):
        self.initial_state = initial_state
        self.final_state = final_state
        self.states = states
        self.transitions = transitions
    def create_transition(self, from_state, to_state, condition):
        new_transition = dict()
        new_transition['from_state'] = from_state
        new_transition['to_state'] = to_state
        new_transition['condition'] = condition
        self.transitions.append(new_transition)

    def display(self):
        print(",".join(self.states))
        print(",".join(set(alphabet)))
        print(self.initial_state)
        print(self.final_state)
        print(self.transitions)

class DFA:
    def __init__(self, initial_state, final_state, states, transitions):
        self.initial_state = initial_state
        self.final_state = final_state
        self.states = states
        self.transitions = transitions

    def create_transition(self, from_state, to_states, condition):
        new_transition = dict()
        new_transition['from_state'] = from_state
        new_transition['to_state'] = to_states
        new_transition['condition'] = condition
        self.transitions.append(new_transition)

    def display(self):
        global dfa_states_mapping, alphabet
        states_mappings = []
        final_states_mappings = []
        transitions_mappings = []
        for state in self.states:
            states_mappings.append(dfa_states_mapping[state])

        for state in self.final_state:
            final_states_mappings.append(dfa_states_mapping[state])

        output_states = ",".join(sorted(states_mappings))
        output_alphabet = ",".join(sorted(set(alphabet)))
        output_initial_state = dfa_states_mapping[tuple(sorted(self.initial_state))]
        output_final_state = ",".join(sorted(final_states_mappings))

        for index, transition in enumerate(self.transitions):
            for letter in alphabet:
                transitions_mappings.append("(" + dfa_states_mapping[transition] + ", " + letter + ", " + dfa_states_mapping[self.transitions[transition][letter]] + ")")

        output_transitions = ",".join(transitions_mappings)
        return output_states, output_alphabet, output_initial_state, output_final_state, output_transitions

def parse_input (lines):
    global alphabet
    customized_transitions = []
    states = lines[0].replace("\n", "").split(",")
    alphabet = lines[1].replace("\n", "").split(",")
    alphabet.remove(" ")
    initial_state = lines[2].replace("\n", "")
    final_state = lines[3].replace("\n", "")
    transitions = lines[4].replace(", ,", ",-,").replace(" ", "").replace(",-,", ", ,")
    transitions = transitions.replace("\n", "").split("),(")
    transitions = [[token.strip() if not (token == " ") else token for token in item.replace("(", "").replace(")", "").split(",")] for item in transitions]
    for transition in transitions:
        transition_object = dict()
        transition_object['from_state'] = transition[0]
        transition_object['to_state'] = transition[2]
        transition_object['condition'] = transition[1]
        customized_transitions.append(transition_object)

    return initial_state, final_state, states, customized_transitions

def epsilon_closure(states):
    global transition_object
    output_states = states.copy()

    for state in output_states:
        try:
            new_states = transition_object[state][" "]
        except:
            new_states = []

        for new_state in new_states:
            if new_state not in output_states:
                output_states.append(new_state)

    return sorted(output_states)


def apply_condition(states, letter):
    global transition_object
    all_destinations = []

    for state in states:
        try:
            all_destinations += transition_object[state][letter]
        except:
            all_destinations += []
    all_destinations = epsilon_closure(all_destinations)
    return all_destinations

def construct_nfa_transitions(transitions_array):
    transitions_dict = dict()
    for transition_element in transitions_array:
        from_state = transition_element['from_state']
        condition = transition_element['condition']
        to_state = transition_element['to_state']
        if from_state in transitions_dict:
            if condition in transitions_dict[from_state]:
                transitions_dict[from_state][condition].append(to_state)
            else:
                transitions_dict[from_state][condition] = [to_state]
        else:
            transitions_dict[from_state] = {condition: [to_state]}
    print(transitions_dict)
    return transitions_dict



def NFA_to_DFA(nfa):
    global alphabet, transition_object, dfa_states_counter, dfa_states_mapping
    dfa_transitions = {}
    dfa_initial_state = epsilon_closure([nfa.initial_state])
    output_dfa = DFA(dfa_initial_state,[],[tuple(sorted(dfa_initial_state))],[])
    for state in output_dfa.states:
        state_tuple = tuple(sorted(state))
        for letter in alphabet:
            destinations = apply_condition(state, letter)
            if len(destinations) == 0:
                destinations = ['DEAD']
            destination_tuple = tuple(sorted(destinations))

            if state_tuple in dfa_transitions:
                dfa_transitions[state_tuple][letter] = destination_tuple
            else:
                dfa_transitions[state_tuple] = {letter: destination_tuple}
                dfa_states_mapping[state_tuple] = "Q" + str(dfa_states_counter)
                dfa_states_counter +=1
            if not (destination_tuple in dfa_transitions):
                output_dfa.states.append(destination_tuple)
    output_dfa.states = sorted(set(output_dfa.states))
    # print(output_dfa.states)
    output_dfa.transitions = dfa_transitions
    output_dfa.final_state = []
    for state in output_dfa.states:
        if nfa.final_state in state:
            output_dfa.final_state.append(state)
    return output_dfa

#------------------------- RUN CODE -----------------------
transition_object= []
alphabet = []
dfa_states_counter = 0
dfa_states_mapping = dict()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')
    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")
    args = parser.parse_args()
    output_file = open("task_2_2_result.txt", "w+")

    with open(args.file, "r") as file:
        lines = file.readlines()
        initial_state, final_state, states, transitions = parse_input(lines)
        transition_object = construct_nfa_transitions(transitions)
        input_nfa = NFA(initial_state, final_state, states, transition_object)
        output_dfa = NFA_to_DFA(input_nfa)
        output_states, output_alphabet, output_initial_state, output_final_state, output_transitions = output_dfa.display()
        output_file.write(output_states + "\n")
        output_file.write(output_alphabet + "\n")
        output_file.write(output_initial_state + "\n")
        output_file.write(output_final_state + "\n")
        output_file.write(output_transitions + "\n")

