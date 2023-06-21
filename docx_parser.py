# import docx # https://github.com/python-openxml/python-docx/ old method

# https://github.com/ShayHill/docx2python/ easier for getting footnotes
from docx2python import docx2python

# extract docx content
with docx2python('powerpoints/example.docx') as docx_content:
    text = docx_content.text
    # print(docx_content.text)

def walk_and_find(string: str, object: str):
    """walks in a string until it finds the object in the string"""
    lenght = len(object)
    for i in range(len(string)-lenght+1):
        if ''.join(string[i:i+lenght]) == object:
            return i, i + lenght
        
    raise Exception(f"{object} wasn't found in the string")


def parse(text: str) -> dict:
    state_dict = {}
    state_dict['countries'] = []
    
    country_index = 0
    body_index = 0
    for line in text.splitlines():
        line = line.lstrip()
        if line == '':
            continue
        if line[:2] == '% ':
            # master title
            state_dict['title'] = line[2:].strip()
            pass
        if line[:3] == '%% ':
            # master subtitle
            state_dict['subtitle'] = line[3:].strip()
            pass
        if line[:2] == '# ':
            # country title
            state_dict['countries'].append({'title': line[2:].strip(), 'body': []})
            country_index += 1
            body_index = 0
        if line[:3] == '## ':
            # country subtitle
            state_dict['countries'][country_index-1]['body'].append({'subtitle': line[2:].strip()})
            body_index += 1
    return state_dict

import json
print(json.dumps(parse(text), indent=2))
# print(walk_and_find("bla bla car lol", "car"))