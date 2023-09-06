import os
import subprocess, sys, tempfile
from word2pptx import transform

transform("tests/ludification.docx", "tests/lud.pdf", 35, 11)


# html = wpx.make_html_doc(wpx.word_tree("tests/RPA.docx"))
# html_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
# html_file.write(html)
# html_file.close()

# title_css = "h1.master-title {font-size: %dpt;}\nh2.master-subtitle {font-size: %dpt;}" % (19.5, 15)
# css_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
# css_file.write(title_css)
# css_file.close()

# if sys.platform == 'win32':
#     Prince = r"C:\Program Files (x86)\Prince\engine\bin\prince.exe"
# else:
#     Prince = "prince"

# subprocess.run([Prince, "-s", "html/boom.css", "-s", css_file.name, html_file.name, "-o", "tests/test.pdf"])    
# os.remove(html_file.name)
# os.remove(css_file.name)

# from pypdf import PdfWriter, PdfReader
# infile = PdfReader('tests/test.pdf', 'rb')
# output = PdfWriter()

# for i in range(2, len(infile.pages)):
#     p = infile.pages[i]
#     output.add_page(p)

# with open('tests/test.pdf', 'wb') as f:
#     output.write(f)