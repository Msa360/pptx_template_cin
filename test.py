import pptx

prs = pptx.Presentation("powerpoints/veille_ai.pptx")


def print_all_text(presentation):
    """print all runs in a presentation"""
    # text_runs will be populated with a list of strings,
    # one for each text run in presentation
    text_runs = []

    for slide in presentation.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.text == "Santé":
                        print(run.font.color.type.__repr__())
                        print(run.font.color.theme_color.__repr__())

                    text_runs.append(run.text)

    print(text_runs[:15])

print_all_text(prs)
# prs.save('test.pptx')
