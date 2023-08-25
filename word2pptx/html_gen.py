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

def head_tags(author: str, title: str, date: str, id: str):
    soup = BeautifulSoup(HTML, 'html.parser')
    soup.find('meta', {'name': 'author'})['content'] = author
    soup.find('title').append(title)
    soup.find('p', class_="date").append(date)
    soup.find('p', class_="article-id").append(id)

    return soup

def make_headcover(title: str, subtitle: str):
    pass

def add_banner(text: str):
    pass

def add_subtitle(text: str):
    pass

def add_paragraphe(text: str):
    pass

def make_bibliography():
    pass

def make_html_doc(tree: dict):
    """makes full html file from parsed word document tree"""
    pass

if __name__ == "__main__":
    soup = head_tags('PH Hugo', 'Les red grooms', '2023', '#00-87-12')
    print(soup.prettify())