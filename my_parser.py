# coding=utf-8
"""importe le module htmlParser
"""
from html.parser import HTMLParser


class HTMLTagParser(HTMLParser):
    """La classe utilisee ici pour le HTMLparser est issue de la classe HTMLParser
            avec les attributs suivants:
            links = liens resolus via href
            links_texts = liens resolus via text

           """
    def __init__(self):
        super().__init__()
        self.reset()
        self.links = []
        self.links_text = []

    def handle_starttag(self, tag, attrs):
        """extrait  balises html et les filtres selon qu'elles soient de types <a>
            si c'est le cas elle les ajoute dans links sinon dans links_texts
        """
        forbidden_tags = ['data-srcset', 'srcset']
        if tag != 'a':
            attr = dict(attrs)
            self.links_text.append(attr)
        else:
            if tag not in forbidden_tags:
                attr = dict(attrs)
                self.links.append(attr)
