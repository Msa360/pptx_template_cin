"""Handles word document input parsing"""

# import docx # https://github.com/python-openxml/python-docx/ old method

from docx2python import docx2python # https://github.com/ShayHill/docx2python/ easier for getting footnotes
import re
import json



SUPERSCRIPTS = {
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
    """walks in a string until it finds the object in the string, then return start to end+1"""
    lenght = len(object)
    for i in range(len(string)-lenght+1):
        if string[i:i+lenght] == object:
            return i
        
    return -1

def superscript_footnotes(text: str):
    """makes the footnotes appear as superscripts"""
    pattern = r"----footnote([0-9]{1,3})----"
    if re.search(r"----footnote1----", text): # this is because of the bug when the footnote1 is skipped
        return re.sub(pattern, lambda m: "".join(SUPERSCRIPTS[char] for char in m.group(1)), text)
    else:
        # substract 1 to all footnotes since footnote1 was skipped else it would start at 2
        return re.sub(pattern, lambda m: "".join(SUPERSCRIPTS[char] for char in str(int(m.group(1)) - 1)), text)


def parse(text: str) -> dict:
    state_dict = {
        'author': '',
        'title': '',
        'subtitle': '',
        'body': [],
        'sources': []
    }

    for line in text.splitlines():
        line = line.lstrip()
        if line == '':
            continue
        
        elif line[:2] == '@ ':
            # author
            state_dict['author'] = line[2:].strip()

        elif line[:2] == '% ':
            # master title
            state_dict['title'] = line[2:].strip()

        elif line[:3] == '%% ':
            # master subtitle
            state_dict['subtitle'] = line[3:].strip()

        elif line[:2] == '# ':
            # title
            state_dict['body'].append({'type': 'title', 'content': line[2:].strip()})

        elif line[:3] == '## ':
            # subtitle
            state_dict['body'].append({'type': 'subtitle', 'content': line[3:].strip()})

        elif re.search(r"footnote([0-9]{1,3})\)", line):
            # source from footnote
            line = re.sub(r"footnote([0-9]{1,3})\)", lambda m: "".join(char for char in m.group(1)), line)
            num, source = line.split('\t', 1)
            state_dict['sources'].append(source.strip())
        elif  line.strip() == "endnote1)":
            continue # this is of the word online to word bug that creates endnote1
        else:
            # text paragraph
            state_dict['body'].append({'type': 'text', 'content': line.strip()})

    return state_dict

def sources_correction(sources: list[str]):
    """
    Docx from word online to word often create an extra empty footnote
    so this function corrects this behavior 
    """
    if sources[0] == "":
        sources.pop(0)

    for i in range(len(sources)):
        n = walk_and_find(sources[i], '<a href="')
        if n >= 0:
            index = walk_and_find(sources[i][n+9:], "\"")
            sources[i] = sources[i][n+9:n+9+index]

    return sources

def word_tree(filepath: str):
    """
    Takes the word file path and creates a tree from it
    """
    with docx2python(filepath) as docx_content:
        text = docx_content.text
    text = superscript_footnotes(text)
    state_dict = parse(text)
    state_dict['sources'] = sources_correction(state_dict['sources'])
    return state_dict

if __name__ == "__main__":
    state_dict = word_tree('tests/RPA.docx')
    with open("temp_tree.json", 'w') as f:
        json.dump(state_dict, f, indent=2)