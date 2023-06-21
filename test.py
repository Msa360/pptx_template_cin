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
                    if run.text not in ["Canada", "France", "États-Unis", "Royaume-Uni", "Sources"]:
                        # print(run.text)
                        # print(f"{run.font.color.type=}")
                        # print(f"{run.font.color.theme_color=}")
                        # print(f"{shape.height=}")
                        print(f"{shape.width=}")
                        print(f"{shape.left=}")


                    text_runs.append(run.text)

    # print(text_runs[:15])

print_all_text(prs)
# prs.save('test.pptx')
