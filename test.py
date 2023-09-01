import subprocess
import word2pptx as wpx


html = wpx.make_html_doc(wpx.word_tree("tests/RPA.docx"))
with open("tests/temp.html", "w") as f:
    print(html, file=f)


title_css = """
h1.master-title { font-size: %dpt; }
h2.master-subtitle { font-size: %dpt; }
""" % (18.5, 15)
with open("tests/temp.css", "w") as f:
    print(title_css, file=f)

subprocess.run(["prince", "-s", "html/boom.css", "-s", "tests/temp.css", "tests/temp.html", "-o", "tests/test.pdf"])