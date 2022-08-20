import json, html
from pathlib import Path
from wtp_nlp.__main__ import language_processor 
from wtp_nlp.data.metro_stations import *
from wtp_nlp.data.tokens import *
from wtp_nlp.data import status

from bs4 import BeautifulSoup

class TestHistorical:
    def get_history(self, index):
        with open(Path(__file__) / '..' / 'history.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
        body = html.unescape(history[index]['body'])
        soup = BeautifulSoup(body, 'html.parser')
        processed_html = [s for s in soup.strings]
        text = ' '.join(processed_html)
        return text

        # self.indexes = [17, 19, 20, 35, 66]

    def test_17(self):
        result = language_processor(self.get_history(17))
        assert result == [
            {
                'name': 'relation',
                'matched': [C6, 1, Between, 1, C17],
                'processed_to': NotImplemented
            },
            {
                'name': 'relation',
                'matched': [C18, 1, Between, 1, C18],
                'processed_to': NotImplemented
            },
            {
                'name': 'shortened_service',
                'matched': [Shortened_Service, 0, On, 2, C6, 1, Between, 1, C17],
                'processed_to': (status.Loop, [C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17])
            },
            {
                'matched': [Not_Functioning_Station, 1, C18],
                'name': 'station_closed',
                'processed_to': NotImplemented
            },
        ]

    def test_19(self):
        result = language_processor(self.get_history(19))
        assert result[0]['processed_to'] == (status.Facilities, C8)

    def test_20(self):
        result = language_processor(self.get_history(20))
        assert result[2]['processed_to'] == (status.Loop, [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A13, A14, A15, A17, A18, A19, A20])

    def test_35(self):
        result = language_processor(self.get_history(35))
        assert result[7]['processed_to'] == (status.Loop, [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A13, A14, A15, A17, A18, A19, A20])

    def test_66(self):
        result = language_processor(self.get_history(66))
        assert result[3]['processed_to'] == (status.Loop, [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A13, A14, A15, A17, A18, A19, A20])

    def test_73(self):
        result = language_processor(self.get_history(73))
        assert result[4]['processed_to'] == (status.Loop, [A7, A8, A9, A10, A11, A13, A14, A15, A17, A18, A19, A20, A21, A22, A23])        
            
# TestHistorical.test_17()