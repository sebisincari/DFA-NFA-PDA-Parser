from collections import deque

def get_rules(vec):
    d = {}
    lenn = len(vec)
    for i in range(0,lenn,8):
        state = vec[i]
        next_state = vec[i+2]
        inpt = vec[i+3]
        stack_top = vec[i+5]
        stack_replace = vec[i+7]
        tuplu_stanga = (state,inpt,stack_top)
        tuplu_dreapta = (next_state,stack_replace)
        if tuplu_stanga not in d:
            d[tuplu_stanga] = tuplu_dreapta
        else:
            print("Sectiunea Delta fault! Invalid data.")

    return d

def pda_checker(string, rules, sections):
    valid = True
    stack = deque()
    states = sections["States"]
    i = states.index("s")
    current_state = states[i - 1]

    stack_top = '$'
    index = 0
    lenn = len(string)

    while (index < lenn or valid):
        valid = False
        if (current_state,'$','$') in rules:
            (state,stack_val)=rules[(current_state,'$','$')]
            valid = True
            current_state = state
            if stack_val != '$':
                stack.append(stack_val)
                stack_top = stack_val
        elif (current_state,'$',stack_top) in rules:
            (state,stack_val)=rules[(current_state,'$',stack_top)]
            valid = True
            current_state = state
            stack.pop()
            if len(stack) != 0:
                stack_top = stack.pop()
                stack.append(stack_top)
            else:
                stack_top = '$'
            if stack_val != '$':
                stack.append(stack_val)
                stack_top = stack_val
        if index < lenn:
            if (current_state,string[index],'$') in rules:
                (state,stack_val) = rules[(current_state,string[index],'$')]
                valid = True
                current_state = state
                index += 1
                if stack_val != '$':
                    stack.append(stack_val)
                    stack_top = stack_val
            elif (current_state,string[index],stack_top) in rules:
                (state,stack_val) = rules[(current_state,string[index],stack_top)]
                valid = True
                current_state = state
                index += 1
                stack.pop()
                if len(stack) != 0:
                    stack_top = stack.pop()
                    stack.append(stack_top)
                else:
                    stack_top = '$'
                if stack_val != '$':
                    stack.append(stack_val)
                    stack_top = stack_val

    if current_state in sections["Finals"] and len(stack) == 0:
        print("String accepted!")
    else:
        print("String not accepted!")
