"""
Library for transforming a Word document (.docx) into PDF
"""

from word2pptx.html_gen import *
from word2pptx.docx_parser import *



def transform(input: str, ouput: str, title_size: float, subtitle_size: float):
    """
    ### The primary function
    
    input is the Word document

    output is the PDF
    """

    import subprocess, sys, tempfile, os

    html = make_html_doc(word_tree(input))
    html_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    html_file.write(html)
    html_file.close()

    css = "h1.master-title {font-size: %dpt;}\nh2.master-subtitle {font-size: %dpt;}" % (title_size, subtitle_size)
    css_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    css_file.write(css)
    css_file.close()

    if sys.platform == 'win32':
        Prince = r"C:\Program Files (x86)\Prince\engine\bin\prince.exe"
    else:
        Prince = "prince"

    subprocess.run([Prince, "-s", "html/boom.css", "-s", css_file.name, html_file.name, "-o", ouput])    
    os.remove(html_file.name)
    os.remove(css_file.name)

    from pypdf import PdfWriter, PdfReader
    infile = PdfReader(ouput, 'rb')
    outfile = PdfWriter()

    # remove first 2 pages
    for i in range(2, len(infile.pages)):
        p = infile.pages[i]
        outfile.add_page(p)

    with open(ouput, 'wb') as f:
        outfile.write(f)