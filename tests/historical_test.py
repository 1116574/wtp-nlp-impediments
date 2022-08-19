import json, html
from pathlib import Path

from wtp_nlp.__main__ import language_processor 

from bs4 import BeautifulSoup

class Historical_Tests:
    def __init__(self):
        with open(Path(__file__) / '..' / 'history.json', 'r', encoding='utf-8') as f:
            self.history = json.load(f)

        self.indexes = [17, 19, 20, 35, 66]

    def test_indexes(self):
        for index in self.indexes:
            body = html.unescape(self.history[index]['body'])
            soup = BeautifulSoup(body, 'html.parser')
            processed_html = [s for s in soup.strings]

            text = ' '.join(processed_html)
            print(language_processor(text))
            assert 1 == 1
            