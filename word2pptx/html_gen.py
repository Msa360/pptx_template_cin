"""Generating the html code"""
from bs4 import BeautifulSoup

HTML = """<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN">
<html lang="fr">
<head>
  <title></title>
  <meta name="author" content=""/>
  <meta name="subject" content="Article de veille"/>
</head>
<body>
<p class="date"></p>
<div><p style="color: red;">This is page should be removed, it is a honeypot for the prince software watermark.</p></div>
<div class="headcover" style="counter-reset: page 1">
  <p class="article-id">Article </p>
  <div class="title-container">
    <h1 class="master-title"></h1>
  </div>
  <div class="subtitle-container">
    <h2 class="master-subtitle"></h2>
  </div>
</div>
</body>"""

def make_head(soup: BeautifulSoup, author: str, title: str, subtitle: str, date: str, id: str):
    soup.find('meta', {'name': 'author'})['content'] = author
    soup.find('title').append(title)
    soup.find('p', class_="date").append(date)
    soup.find('p', class_="article-id").append(id)
    soup.find('h1', class_="master-title").append(title)
    soup.find('h2', class_="master-subtitle").append(subtitle)
    return soup

def add_banner(soup: BeautifulSoup, text: str):
    tag = soup.new_tag('h1', attrs={'class': 'header'})
    tag.append(text)
    soup.find('body').append(tag)
    return soup

def add_subtitle(soup: BeautifulSoup, text: str):
    tag = soup.new_tag('h2', attrs={'class': 'subtitle'})
    tag.append(text)
    soup.find('body').append(tag)
    return soup

def add_paragraphe(soup: BeautifulSoup, text: str):
    tag = soup.new_tag('p')
    tag.append(text)
    soup.find('body').append(tag)
    return soup

def make_bibliography(soup: BeautifulSoup, sources: list):
    bib = BeautifulSoup("""<div class="bibliography"><h1 class="header">Sources</h1><ol></ol></div>""", 'html.parser')
    ol = bib.find('ol')
    for source in sources:
        tag = bib.new_tag('li')
        tag.append(source)
        ol.append(tag)
    soup.find('body').append(bib)
    return soup

def make_backcover(soup: BeautifulSoup, author: str):
    backcover = f"""
    <div class="backcover">
    <div class="author">{author}</div>
    <div class="contact">
      Pour nous contacter:<br>
      <a href="mailto:centre.innovation.numerique@saaq.gouv.qc.ca" style="color: #f6d677;">
        centre.innovation.numerique@saaq.gouv.qc.ca
      </a>
    </div>
    </div>
    """
    soup.find('body').append(BeautifulSoup(backcover, 'html.parser'))
    return soup

def make_html_doc(tree: dict, date: str):
    """makes full html file from parsed word document tree"""
    soup = BeautifulSoup(HTML, 'html.parser')
    soup = make_head(soup, tree['author'], tree['title'], tree['subtitle'], date, tree['id'])
    for part in tree['body']:
        if part['type'] == 'title':
            soup = add_banner(soup, part['content'])
        elif part['type'] == 'subtitle':
            soup = add_subtitle(soup, part['content'])
        elif part['type'] == 'text':
            soup = add_paragraphe(soup, part['content'])
    soup = make_bibliography(soup, tree['sources'])
    soup = make_backcover(soup, tree['author'])
    return soup.prettify()

if __name__ == "__main__":
    import docx_parser

    html_code = make_html_doc(docx_parser.word_tree("tests/RPA.docx"), "20-23-2023")
    print(html_code)