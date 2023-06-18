from pptx.enum.text import PP_ALIGN
import pptx
import copy
from pptx.shapes.autoshape import Shape
from utils import add_country, delete_shape, find_template_shape

test_parsed_dict = {
    "title": "IoT",
    "subtitle": "Internet of things",
    "countries": [
        {
            "title": "France",
            "body": [
                {"subtitle": "Introduction", "text": "La France est un beau pays!"*14},
                {"subtitle": "Description", "text": "La France est vraiment un super beau pays!"*12}
            ]
        },
        {"title": "Allemagne", "body": [{"subtitle": None, "text": "L'allemagne est un beau pays!"}]}
    ],
    "sources": [{"number": "1", "text": "www.example1.com"}, {"number": "2", "text": "www.example2.com/thisisanexample?iot=1"}]
}

def clone_shape(shape, left, top, width, height):
    """Add a duplicate of `shape` to the slide on which it appears."""
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



    
# print(text_runs[:30])
prs = pptx.Presentation("powerpoints/gabarit_mod.pptx")
banner = list(find_template_shape(prs, "banner"))[0]
top = 100000
for country in test_parsed_dict["countries"]:
    bottom = add_country(prs, prs.slides[-1], country, banner, top)
    top = bottom + 100000
delete_shape(banner, prs.slides[-1])
prs.save('powerpoints/test.pptx')

