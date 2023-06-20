from pptx.enum.text import PP_ALIGN
import pptx
import copy
from pptx.shapes.autoshape import Shape
from utils import add_countries, delete_shape, find_template_shape, clone_shape

test_parsed_dict = {
    "title": "IoT",
    "subtitle": "Internet of things",
    "countries": [
        {
            "title": "France",
            "body": [
                {"subtitle": "Introduction", "text": "La France est un beau pays! "*14},
                {"subtitle": "Description", "text": "La France est vraiment un super beau pays! "*12}
            ]
        },
        {"title": "Australie", "body": [{"subtitle": None, "text": "L'allemagne est un beau pays! "*14}]},
        {"title": "Canada", "body": [{"subtitle": None, "text": "L'allemagne est un beau pays! "*14}]},
        {"title": "Kenya", "body": [{"subtitle": None, "text": "L'allemagne est un beau pays! "*14}]},
        {"title": "Belgique", "body": [{"subtitle": None, "text": "L'allemagne est un beau pays! "*14}]}
    ],
    "sources": [{"number": "1", "text": "www.example1.com"}, {"number": "2", "text": "www.example2.com/thisisanexample?iot=1"}]
}




prs = pptx.Presentation("powerpoints/gabarit_mod.pptx")
# print(next(find_template_shape(prs.slides[0], "banner")))
top = 100000
bottom = add_countries(prs, prs.slides[-1], test_parsed_dict["countries"], top)
# delete_shape(banner, prs.slides[-1]) # todo: implement a clean up function
delete_shape(next(find_template_shape(prs.slides[1], "banner")), prs.slides[1])
prs.save('powerpoints/test.pptx')

