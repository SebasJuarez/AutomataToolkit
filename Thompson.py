import re

def epsilon_closure(states, nfa_transitions, epsilon):
    closure = set(states)
    stack = list(states)
    
    while stack:
        state = stack.pop()
        if epsilon in nfa_transitions[state]:
            transitions = nfa_transitions[state][epsilon]
            if isinstance(transitions, int):
                transitions = [transitions]
            for next_state in transitions:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
    
    return closure


class Thompson:
    
    def __init__(self, epsilon='ε', concat_operator="."):
        self.epsilon = epsilon
        self.concat_operator = concat_operator
        
    def convert2NFA(self, postfix_expression):
        regex = postfix_expression

        # Obtiene todos los símbolos únicos y añade el épsilon
        keys = list(set(re.sub('[^A-Za-z0-9]+', '', regex) + self.epsilon))

        states = []
        stack = []
        counter = -1
        c1 = 0
        c2 = 0

        for i in regex:
            if i in keys:  # Símbolo terminal
                counter += 1
                c1 = counter
                counter += 1
                c2 = counter
                states.append({})
                states.append({})
                stack.append([c1, c2])
                states[c1][i] = c2
                # print(f"Transición añadida: Estado {c1} -> Estado {c2} con símbolo '{i}'")

            elif i == '*':  # Cierre de Kleene
                if stack:
                    r1, r2 = stack.pop()
                    counter += 1
                    c1 = counter
                    counter += 1
                    c2 = counter
                    states.append({})
                    states.append({})
                    stack.append([c1, c2])
                    states[r2][self.epsilon] = [r1, c2]
                    states[c1][self.epsilon] = [r1, c2]
                    # print(f"Transiciones epsilon añadidas: Estado {r2} -> {r1}, {c2} y Estado {c1} -> {r1}, {c2}")

            elif i == self.concat_operator:  # Concatenación
                if len(stack) >= 2:
                    r21, r22 = stack.pop()  # Segundo símbolo
                    r11, r12 = stack.pop()  # Primer símbolo
                    states[r12][self.epsilon] = r21  # Transición epsilon
                    stack.append([r11, r22])
                    # print(f"Concatenación realizada: Estado {r12} -> {r21} con símbolo ε")

            elif i == "+" or i == "|":  # Unión
                if len(stack) >= 2:
                    counter += 1
                    c1 = counter
                    counter += 1
                    c2 = counter
                    states.append({})
                    states.append({})
                    r11, r12 = stack.pop()
                    r21, r22 = stack.pop()
                    stack.append([c1, c2])
                    states[c1][self.epsilon] = [r21, r11]
                    states[r12][self.epsilon] = [c2]
                    states[r22][self.epsilon] = [c2]
                    # print(f"Unión realizada: Nuevo estado inicial {c1}, nuevo estado final {c2}")

        start_state, accept_state = stack[0][0], stack[-1][1]
        
        return (keys, states, start_state, accept_state)

    def get_formatted_afn_params(self, afn: tuple) -> tuple:
        nfa_symbols, nfa_og_transitions, nfa_start, nfa_end = afn
        nfa_end = {nfa_end}
        nfa_states = [i for i in range(len(nfa_og_transitions))]
        nfa_transitions = {}
        for i in range(len(nfa_og_transitions)):
            new_transition = {}
            for symbol in nfa_symbols:
                if nfa_og_transitions[i].get(symbol) is not None:
                    next_states = nfa_og_transitions[i].get(symbol)
                    new_transition[symbol] = next_states if isinstance(next_states, list) else [next_states]
            nfa_transitions[i] = new_transition
            
        return (nfa_symbols, nfa_states, nfa_transitions, nfa_start, nfa_end)
    
    def print_nfa(self, nfa):
        keys, states, start, end = nfa
        print("Estados:")
        for i in range(len(states)):
            print(f"Estado {i}")
        
        print("\nSímbolos:")
        for key in keys:
            print(key)
        
        print("\nEstado Inicial:")
        print(start)
        
        print("\nEstado de Aceptación:")
        print(end)
        
        print("\nTransiciones:")
        for i, state in enumerate(states):
            for symbol, next_state in state.items():
                if isinstance(next_state, list):
                    for ns in next_state:
                        print(f"Estado {i} -> Estado {ns} con símbolo '{symbol}'")
                else:
                    print(f"Estado {i} -> Estado {next_state} con símbolo '{symbol}'")
    
    def process_input(self, input_strings, nfa):
        keys, states, start, end = nfa
        epsilon = self.epsilon
        
        if not isinstance(end, set):
            end = {end}
        
        print("Iniciando simulacion en AFN...")
        for input_string in input_strings:
            current_states = epsilon_closure({start}, states, epsilon)
            # Los prints se pueden descomentar si es que se quiere ver el proceso del analisis en la simulación.
            # print(f"\nProcesando cadena: '{input_string}'")
            # print(f"Estados iniciales: {current_states}")
            
            for symbol in input_string:
                next_states = set()
                # print(f"Procesando símbolo: '{symbol}'")
                
                for state in current_states:
                    if symbol in states[state]:
                        transitions = states[state][symbol]
                        if isinstance(transitions, list):
                            next_states.update(transitions)
                        else:
                            next_states.add(transitions)
                current_states = epsilon_closure(next_states, states, epsilon)
                # print(f"Estados actuales después de procesar '{symbol}': {current_states}")
            
            if end & current_states:
                print(f"'{input_string}' SÍ es aceptada")
            else:
                print(f"'{input_string}' NO es aceptada")
