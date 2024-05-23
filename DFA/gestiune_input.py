def load_file_cont(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    final_str = []
    for line in lines:
        while line[0] == ' ':
            line = line[1:]
        if line[0] == '#':
            line = ""
        i = 0
        index = -1
        index = line.find("#")
        if index != -1:
            line = line[:index]
        if line[-1] == ',':
            line = line[:-1]
        final_str.append(line)
        
    while "" in final_str:
            final_str.remove("")
    
    return final_str


def get_section_lst(content):
    d={}
    sec_name = ""
    file = content
    for elements in file:
        if elements[0] == '[' and elements[-2] == ']':
            sec_name = elements[1:-2]
            d[sec_name] = []
        else:
            elements = elements.split()
            for element in elements:
                if element[-1] == ',':
                    element=element[:-1]
                if sec_name != "":
                    d[sec_name].append(element)
                    
    return d


def get_section_cont(name, content):
    return(content[name])
