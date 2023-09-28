"""
Library for transforming a Word document (.docx) into PDF
"""

from word2pptx.html_gen import *
from word2pptx.docx_parser import *
import os, sys, subprocess

__all__ = ["transform"]

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def check_prince():
    """checks if Prince is installed"""
    if sys.platform == 'win32':
        Prince = r"C:\Program Files (x86)\Prince\engine\bin\prince.exe"
    else:
        Prince = "prince"

    try:
        subprocess.run([Prince, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except:
        raise Exception("You need to install Prince software") 
    

def transform(input: str, ouput: str, date: str, title_size: float = 24, subtitle_size: float = 10, img_path: str = None):
    """
    ### The primary function
    
    input is the Word document

    output is the PDF
    """
    check_prince() # checks if prince is installed

    import tempfile

    html = make_html_doc(word_tree(input), date, img_path)
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

    subprocess.run([Prince, "-s", resource_path(os.path.join("html","boom.css")), "-s", css_file.name, html_file.name, "-o", ouput])    
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