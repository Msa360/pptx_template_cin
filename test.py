import subprocess
import word2pptx as wpx


html = wpx.make_html_doc(wpx.word_tree("tests/RPA.docx"))
with open("tests/temp.html", "w") as f:
    print(html, file=f)

subprocess.run(["prince", "-s", "html/boom.css", "tests/temp.html", "-o", "tests/test.pdf"])