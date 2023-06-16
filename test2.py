from pptx.enum.text import PP_ALIGN
import pptx
import copy
from pptx.shapes.autoshape import Shape

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


def find_template_shape(prs, markup):
    """markup is the template placeholder"""
    used = 0
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                if paragraph.text == markup and used < 1:
                    print("found matching text")

                    # new_shape = clone_shape(shape, prs.slide_width*0.1, prs.slide_height*0.5, shape.width*1.52, shape.height)
                    # new_shape.top = int(1.5*new_shape.top)
                    # slide.shapes._spTree.remove(new_shape._element) # to delete a shape

                    used += 1 # very important else got duplicate

    prs.save('powerpoints/test.pptx')
# print(text_runs[:30])
prs = pptx.Presentation("powerpoints/output.pptx")
find_template_shape(prs, 'Titre de l’article')


