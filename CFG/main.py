from gestiune_input import load_file_cont , get_section_lst , get_section_cont
from rules import rule,generator

content = load_file_cont("input.cfg")
sections = get_section_lst(content)#hash cu sectiunile
rules = rule(sections["Rules"])
generator(sections["Rules"][0],rules)


