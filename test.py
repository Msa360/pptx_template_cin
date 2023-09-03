import subprocess, sys
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

if sys.platform == 'win32':
    # windows call to prince:
    subprocess.run([r"C:\Program Files (x86)\Prince\engine\bin\prince.exe", "-s", "html/boom.css", "-s", "tests/temp.css", "tests/temp.html", "-o", "tests/test.pdf"])
else:
    # unix call to prince:
    subprocess.run(["prince", "-s", "html/boom.css", "-s", "tests/temp.css", "tests/temp.html", "-o", "tests/test.pdf"])

from pypdf import PdfWriter, PdfReader
infile = PdfReader('tests/test.pdf', 'rb')
output = PdfWriter()

for i in range(2, len(infile.pages)):
    p = infile.pages[i]
    output.add_page(p)

with open('tests/test.pdf', 'wb') as f:
    output.write(f)