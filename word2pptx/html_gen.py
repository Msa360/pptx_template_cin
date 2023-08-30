"""Generating the html"""
from bs4 import BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')

HTML = """<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN">
<html lang="fr">
<head>
  <title></title>
  <meta name="author" content=""/>
  <meta name="subject" content="Article de veille"/>
  <link rel="stylesheet" type="text/css" href="boom.css"/>
  <link rel="stylesheet" href="https://use.typekit.net/oov2wcw.css"/>
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

def make_bibliography(soup: BeautifulSoup):
    return soup

def make_html_doc(tree: dict):
    """makes full html file from parsed word document tree"""
    soup = BeautifulSoup(HTML, 'html.parser')
    soup = make_head(soup, tree['author'], tree['title'], tree['subtitle'], '2023', '#00-87')
    for part in tree['body']:
        if part['type'] == 'title':
            soup = add_banner(soup, part['content'])
        elif part['type'] == 'subtitle':
            soup = add_subtitle(soup, part['content'])
        elif part['type'] == 'text':
            soup = add_paragraphe(soup, part['content'])
    return soup.prettify()

if __name__ == "__main__":
    # soup = BeautifulSoup(HTML, 'html.parser')
    # soup = make_head(soup, 'PH Hugo', 'Les red grooms', '2023', '#00-87-12')
    # soup = make_headcover(soup, "L'intelligence artificiel", "La matière grise")
    # soup = add_banner(soup, "L'Amérique")
    # soup = add_subtitle(soup, "Le web 3.0")
    # soup = add_paragraphe(soup, 'The Web is a vast collection of documents on the <dfn id="dfn-internet">Internet</dfn> th')
    html_code = make_html_doc({
        "author": "Philippe Gueu",
        "title": "article title here",
        "subtitle": "article subtitle here",
        "body": [
            {"type": "title", "content": "France"},
            {"type": "subtitle", "content": "subtitle here"},
            {"type": "title", "content": "France"},
            {"type": "text", "content": "L'Amérique est là."}
        ],
        "sources": [
            "www.example.com",
            "www.example2.com"
        ]
    })
    print(html_code)