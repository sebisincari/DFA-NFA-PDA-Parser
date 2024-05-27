from gestiune_input import load_file_cont,get_section_lst,get_section_cont
from pda import get_rules, pda_checker

content = load_file_cont("input.cfg")
section_lst = get_section_lst(content)
inpt=input()
rules=get_rules(section_lst["Delta"])
pda_checker(inpt,rules,section_lst)