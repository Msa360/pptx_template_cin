import pptx
from pptx import Presentation
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
from typing import Union
from utils import (
    chunck_text, 
    is_slide_full, 
    remove_newlines, 
    textbox_height_estimate
    )


def add_text_boxes_to_powerpoint(input_file: str, texts: Union[list, tuple], interval: float = 0, output_file="powerpoints/output.pptx"):
    """
    interval between 0 and 1
    """
    prs = Presentation(input_file)

    SLIDE_LAYOUT = 4 # 6 is a blank one, 4 is good
    MAX_CHARS_PER_LINE = 97 # approximate, experimentally determined

    # Create a new slide
    slide_layout = prs.slide_layouts[SLIDE_LAYOUT]
    slide = prs.slides.add_slide(slide_layout)

    # Calculate the width and height of the text boxes
    slide_width = prs.slide_width
    slide_height = prs.slide_height
    textbox_width = slide_width * 1
    # textbox_height = slide_height * 0.2

    # Calculate the position of the text boxes
    textbox_top = slide_height * 0.2
    textbox_left = (slide_width - textbox_width) / 2

    # Iterate through each text and add it to a new text box
    for i, text in enumerate(texts):

        # textbox height depends of the number of chars
        textbox_height = slide_height * textbox_height_estimate(text)

        if is_slide_full(prs, textbox_top, textbox_height):
            print("new slide at", i)
            # Create a new slide if the current slide is full
            slide_layout = prs.slide_layouts[SLIDE_LAYOUT]  # Choose the layout for the new slide
            slide = prs.slides.add_slide(slide_layout)
            textbox_top = slide_height * 0.2
        else:
            # Use the current slide if there is available space
            slide = prs.slides[-1]

        textbox = slide.shapes.add_textbox(textbox_left, textbox_top, textbox_width, textbox_height)

        text_frame = textbox.text_frame
        # text_frame.word_wrap = True
        # text_frame.auto_size = MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT
        # text_frame.fit_text()
        p = text_frame.add_paragraph()
        p.font.size = pptx.util.Pt(10)
        p.text = chunck_text(remove_newlines(text), MAX_CHARS_PER_LINE)
        p.alignment = PP_ALIGN.CENTER

        # if i == 4:
        #     for i in range(10):
        #         p = text_frame.add_paragraph()
        #         p.text = text
        #         p.alignment = PP_ALIGN.CENTER

        # Increase the position for the next text box
        textbox_top += textbox_height + (slide_height * interval)

    prs.save(output_file)
    print(f"Text boxes added. Saved as {output_file}")





# Define the list of texts to add to the PowerPoint presentation
texts = [
# {"Title":"Hello"},
# {"H1":"This is a test"},
# {"H2":"Python is awesome!"},
"This is a test",
"Python is awesome!",
"This is cool!",
"""Python is \nreally awesome!
it is so cool, Python is too awesome! lipsum
orepsum so cool, it is too awesome! lipsummi
it is so cool, Python is too awesome! lipsum
orepsum so cool, it is too awesome! lipsummi
""",
"""Python is bfhjewqhfewflewqhlfbewhqlbhjfew qreally ewq feqwiu eqwhfeuilw  iufh ewlh qwl hufewh u fiew oqhueiwqh uefqwl  awesome!
it is so cool, Python is too awesome! lipsum it is so cool, Python is twesome! lipsum it is so cool, Python is too awesome! lipsum ç, Python is too awesome! lipsum
orepsum so cool, it is too awesome! lipsummii t is so cool, Python is too awesome! lipsum it is so cool, Python is too awesome! lipsum
it is so cool, Python is too awesome! lsum it is so cool, Python is too awesome! lipsum it is so cool, Python is too awesome! lipsum frewg fwe qof  qwouihf
orepsum so cool, it is too awesome! lipsummi euiwoqfhi qwiufewiluqoi u hfewiqu  kquhi lf huilhuilfewqhui l uilwefqh uilfew hil wqehuilfhie huifqwlk
"""*2,
"""Python is bfhjewqhfewflewqhlfbewhqlbhjfew qreally ewq feqwiu eqwhfeuilw  iufh ewlh qwl hufewh u fiew oqhueiwqh uefqwl  awesome!
it is so cool, Python is too awesome! lipsum it is so cool, Python is twesome! lipsum it is so cool, Python is too awesome! lipsum ç, Python is too awesome! lipsum
orepsum so cool, it is too awesome! lipsummii t is so cool, Python is too awesome! lipsum it is so cool, Python is too awesome! lipsum
it is so cool, Python is too awesome! lsum it is so cool, Python is too awesome! lipsum it is so cool, Python is too awesome! lipsum frewg fwe qof  qwouihf
orepsum so cool, it is too awesome! lipsummi euiwoqfhi qwiufewiluqoi u hfewiqu  kquhi lf huilhuilfewqhui l uilwefqh uilfew hil wqehuilfhie huifqwlk
"""*5,
"Python is so awesome!!!"
]

# Call the function with the PowerPoint file and list of texts
add_text_boxes_to_powerpoint("powerpoints/gabarit_veille.pptx", texts, interval=0.05)


