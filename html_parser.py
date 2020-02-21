from html.parser import HTMLParser


class HTMLTagParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.reset()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attr = dict(attrs)
        self.links.append(attr)


class HTMLTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.links_text = []

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            attr = dict(attrs)
            self.links_text.append(attr)
