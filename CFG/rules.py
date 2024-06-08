import random

def rule(vec):
    d={}
    lenn = len(vec)
    for i in range(0,lenn,3): 
        if vec[i] not in d:
            d[vec[i]] = [vec[i+2]]
        else:
            d[vec[i]].append(vec[i+2])
    return d

def generator(str,reguli):
    var=True
    print(str)
    while var:
        var = False
        lenn = len(str)
        newStr = ""
        for i in range(0,lenn):
            if str[i] in reguli:
                #print("aici")
                var=True
                rnd = random.randint(0,len(reguli[str[i]])-1)
                newStr += str[0:i]
                newStr += reguli[str[i]][rnd]
                newStr += str[i+1:]
        print(newStr)
        str = newStr