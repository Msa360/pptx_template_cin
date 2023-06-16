import copy
from pptx.shapes.autoshape import Shape


def chunck_text(text: str, lenght: int):
    """chuncks the text into lines that are smaller or equal than 'lenght' arg"""
    text = list(text)
    text_list = list(text)
    # for i in range(len(text) // lenght):  # iter over lines
    pos = 0
    while len(text_list) / lenght > 1:
        for j in reversed(range(0, lenght+1)):    # iter over chars
            if text_list[j] == " ":
                pos += j
                text[pos] = "\n"
                pos += 1
                text_list = text_list[j+1:]
                break
            if j == 0:
                raise Exception(f"Cannot chunck {''.join(text_list[:lenght])}|{text_list[lenght]}, it would break the word at '|'")
    return ''.join(text)

def remove_newlines(text: str):
    new_text = list(text)
    for i in range(len(text)):
        if 0 < i < len(text) - 1:
            if text[i] == '\n':
                if text[i-1] == ' ' and text[i+1] == ' ':
                    new_text[i] = ''
                    new_text[i-1] = ''
                elif text[i-1] == ' ' and text[i+1] != ' ':
                    new_text[i] = ''
                elif text[i-1] != ' ' and text[i+1] == ' ':
                    new_text[i] = ''
                elif text[i-1] != ' ' and text[i+1] != ' ':
                    new_text[i] = ' '
        else:
            if text[i] == '\n':
                new_text[i] = ''
    return new_text

# a very important algo
def textbox_height_estimate(text: str):
    """
    The goal is to estimate the height of the textbox to fit all the characters
    this is needed since pptx api can't do it because it would need a rendering engine
    """
    n_chars = len(text)
    return (max(n_chars - 100, 0)) * 0.00018 + 0.08


def is_slide_full(presentation, textbox_top, textbox_height):
    # Get the last slide in the presentation
    slide = presentation.slides[-1]
    shapes = list(slide.shapes)
    if len(shapes)==0 or presentation.slide_height > textbox_top + textbox_height:
        return False
    else:
        return True
    

def clone_shape(shape, left, top, width, height):
        # gotta be careful since the shape_id is read-only, it keeps the same id so the id isn't unique anymore
        """Add a duplicate of `shape` to the slide on which it appears.
            Once duplicated, id is obselete, use shape._element to have uniqueness
        """
        shape_obj = shape.element
        sp_tree = shape_obj.getparent()
        new_sp = copy.deepcopy(shape_obj)
        sp_tree.append(new_sp)
        new_shape = Shape(new_sp, None) #(GraphicFrame(new_sp, None) if isinstance(shape, GraphicFrame) else Shape(new_sp, None))
        new_shape.left = int(left)
        new_shape.top = int(top)
        new_shape.width = int(width)
        new_shape.height = int(height)
        return new_shape

def delete_shape(shape, slide):
    slide.shapes._spTree.remove(shape._element)