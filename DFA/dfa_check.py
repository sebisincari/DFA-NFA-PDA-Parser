def validate_dfa(d):
    for cheie,val in d.items():
        if len(val) == 0:
            print(cheie,end=" ")
            print("is empty!")
            return False
    for cheie,val in d.items():
        for v in val:
            if cheie == "Finals":
                if v not in d["States"]:
                    print("Invalid final state!")
                    return False
            elif cheie == "Delta":
                arr = d[cheie]
                lenn = len(arr)
                for i in range (0,lenn,3):
                    fct = arr[i:i+3]
                    if fct[0] not in d["States"] or fct[2] not in d["States"]:
                        print("Invalid state in Delta!")
                        return False
                    if fct[1] not in d["Sigma"]:
                        print("Invalid letter!")
                        return False
    print("Valid!")
    return True


def transitionFunction(d):
    fct = {}
    lenn = len(d["Delta"])
    for i in range(0,lenn,3): 
        op = d["Delta"][i:i+3]  
        if len(op) == 3:  
            t = (op[0],op[1])
            fct[t] = op[2]
    # print("Transition function:")
    # print(fct)
    return fct


def dfaEmulator(str,d,fct):
    states = d["States"]
    i = states.index("s")
    state = states[i - 1]
    
    index = 0
    lenght = len(str)
    while index<lenght:
        t = (state,str[index])
        state = fct[t]
        index += 1
        
    if state in d["Finals"]:
        print("Accepted!")
    else:
        print("String is not accepted!")   
    