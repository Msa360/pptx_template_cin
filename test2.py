from pptx.enum.text import PP_ALIGN
import pptx
import copy
from pptx.shapes.autoshape import Shape
from utils import add_countries, clean_up_shapes, delete_shape, find_template_shape, clone_shape

test_parsed_dict = {
    "title": "IoT",
    "subtitle": "Internet of things",
    "countries": [
        {
            "title": "France",
            "body": [
                {"subtitle": "Introduction"},
                {"text": "La France est un beau pays! "*14},
                {"subtitle": "Description"},
                {"text": "La France est vraiment un super beau pays! "*12}
            ]
        },
        {"title": "Australie", "body": [{"text": "L'allemagne est une³ beau pays! "*14}]},
        {"title": "Canada", "body": [{"text": "Le Canada de magne est un superbe de beau pays! "*14}]},
        {"title": "Kenya", "body": [{"text": "Le Kenya de magne est un vraiment beau pays! "*14}]},
        {"title": "Belgique", "body": [{"text": "La Belgique est un beau pays! j'y suis allé. "*14}]}
    ],
    "sources": [{"number": "1", "text": "www.example1.com"}, {"number": "2", "text": "www.example2.com/thisisanexample?iot=1"}]
}


prs = pptx.Presentation("powerpoints/gabarit_mod.pptx")
top = 100000
bottom = add_countries(prs, prs.slides[-1], test_parsed_dict["countries"], top)
clean_up_shapes(prs, "<banner>") # deletes the template shapes
prs.save('powerpoints/test.pptx')

