
def walk_and_find(string: str, object: str):
    """walks in a string until it finds the object in the string, then return start to end+1"""
    lenght = len(object)
    for i in range(len(string)-lenght+1):
        if string[i:i+lenght] == object:
            return i, i + lenght
        
    raise Exception(f"{object} wasn't found in the string {string}")

def sources_correction(sources: list[str]):
    """
    Docx from word online to word often create an extra empty footnote
    so this function corrects this behavior 
    """
    if sources[0] == "":
        sources.pop(0)

    for i in range(len(sources)):
        if sources[i].startswith("<a href=\""):
            index = walk_and_find(sources[i][9:], "\"")
            sources[i] = sources[i][9:9+index[0]]

    return sources

print(sources_correction([
    '<a href="https://example.com/about">hey</a>',
    '<a href="https://example.com:443/about?e=7549f&r=hbjdfhkeq">hey</a>',
    '<a href="https://example.com/about">hey</a>',
    '<a href="https://example.com/about">hey</a>',

    ]))