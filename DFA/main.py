from gestiune_input import load_file_cont , get_section_lst , get_section_cont
from dfa_check import validate_dfa, transitionFunction, dfaEmulator
from game import createGraph, createMap

content = load_file_cont("input.cfg")
sections = get_section_lst(content)
function = transitionFunction(sections)
string = input()
#print(function)
print(dfaEmulator(string,sections,function))
#graph = createGraph(function)
#createMap(graph)
