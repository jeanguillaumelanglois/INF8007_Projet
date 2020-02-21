# coding=utf-8
from html.parser import HTMLParser


class HTMLTagParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.reset()
        self.links = []
        self.links_text = []

    def handle_starttag(self, tag, attrs):
        forbidenn_tags = ['data-srcset', 'srcset']
        if tag != 'a':
            attr = dict(attrs)
            self.links_text.append(attr)
        else:
            if not tag in forbidenn_tags:
                attr = dict(attrs)
                self.links.append(attr)


