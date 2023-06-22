# import docx # https://github.com/python-openxml/python-docx/ old method

# https://github.com/ShayHill/docx2python/ easier for getting footnotes
from docx2python import docx2python
import re
import json

superscript_dict = {
        "0": "\u2070",
        "1": "\u00B9",
        "2": "\u00B2",
        "3": "\u00B3",
        "4": "\u2074",
        "5": "\u2075",
        "6": "\u2076",
        "7": "\u2077",
        "8": "\u2078",
        "9": "\u2079"
    }

def walk_and_find(string: str, object: str):
    """walks in a string until it finds the object in the string"""
    lenght = len(object)
    for i in range(len(string)-lenght+1):
        if ''.join(string[i:i+lenght]) == object:
            return i, i + lenght
        
    raise Exception(f"{object} wasn't found in the string")

def supercript_footnotes(text: str):
    """makes the footnotes appear as superscript"""
    pattern = r"----footnote([0-9]{1,3})----"
    return re.sub(pattern, lambda m: "".join(superscript_dict[char] for char in m.group(1)), text)

def parse(text: str) -> dict:
    state_dict = {}
    state_dict['countries'] = []
    state_dict['intro'] = []

    
    country_index = 0
    for line in text.splitlines():
        line = line.lstrip()
        if line == '':
            continue
        elif line[:2] == '% ':
            # master title
            state_dict['title'] = line[2:].strip()

        elif line[:3] == '%% ':
            # master subtitle
            state_dict['subtitle'] = line[3:].strip()

        elif line[:2] == '# ':
            # country title
            state_dict['countries'].append({'title': line[2:].strip(), 'body': []})
            country_index += 1
        elif line[:3] == '## ':
            if country_index > 0:
                # country subtitle
                state_dict['countries'][country_index-1]['body'].append({'subtitle': line[3:].strip()})
            else:
                # intro subtitle
                state_dict['intro'].append({'subtitle': line.strip()})
        else:
            # text paragraph
            if country_index == 0:
                state_dict['intro'].append({'text': line.strip()})
            else:
                state_dict['countries'][country_index-1]['body'].append({'text': line.strip()})
    return state_dict


if __name__ == "__main__":
    with docx2python('powerpoints/example.docx') as docx_content:
        text = docx_content.text
        # print(docx_content.text)
        supercript_footnotes(text)
    
    # with open("temp.json", 'w') as f:
    #     json.dump(parse(text), f, indent=2)

    # print(walk_and_find("bla bla car lol", "car"))