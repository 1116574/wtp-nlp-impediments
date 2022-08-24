from wtp_nlp import __main__

import json, html
from pathlib import Path

from bs4 import BeautifulSoup

class Args:
    def __init__(self, text, out) -> None:
        self.text = text
        self.out = out
        self.debug_tokenizer = False
        self.debug_pattern = False
        self.out_file = False
        self.verbosity = 3


def test_json():
    args = Args('Z powodu awarii metro kursuje w pętli Słodowiec-Marymont. Uruchomiono linię zastępczą ZM1', 'json')
    assert __main__.main(args) == {'conditions': [{'status': 'Loop', 'affected': [{'name': 'Marymont', 'id': 'A19'}, {'name': 'Słodowiec', 'id': 'A20'}]}], 'reason': 'awari', 'replacement_service': {'exists': True, 'name': 'ZM1', 'by_extension': False}}


def test_json_multiple_conditions():
    args = Args('Z powodu awarii metro M1 kursuje w pętli Słodowiec-Marymont, a M2 w pętli Trocka-Dw.Wileński. Uruchomiono linię zastępczą ZM1', 'json')
    assert __main__.main(args) == {
        "conditions": [
            {
                "status": "Loop",
                "affected": [
                    {
                        "name": "Marymont",
                        "id": "A19"
                    },
                    {
                        "name": "S\u0142odowiec",
                        "id": "A20"
                    }
                ]
            },
            {
                "status": "Loop",
                "affected": [
                    {
                        "name": "Dworzec Wile\u0144ski",
                        "id": "C15"
                    },
                    {
                        "name": "Szwedzka",
                        "id": "C16"
                    },
                    {
                        "name": "Targ\u00f3wek Mieszkaniowy",
                        "id": "C17"
                    },
                    {
                        "name": "Trocka",
                        "id": "C18"
                    }
                ]
            }
        ],
        "reason": "awari",
        "replacement_service": {
            "exists": True,
            "name": "ZM1",
            "by_extension": False
        }
    }


class TestHistorical:
    def get_history(self, index):
        with open(Path(__file__) / '..' / 'history.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
        body = html.unescape(history[index]['body'])
        soup = BeautifulSoup(body, 'html.parser')
        processed_html = [s for s in soup.strings]
        text = ' '.join(processed_html)
        return text

    def test_18(self):
        result = __main__.main(Args(self.get_history(18), 'json'))
        # print(result)
        assert result == {'conditions': [{'status': 'Double_Loop', 'affected': [[{'name': 'Rondo ONZ', 'id': 'C10'}, {'name': 'Świętokrzyska', 'id': 'C11'}, {'name': 'Nowy Świat-Uniwersytet', 'id': 'C12'}, {'name': 'Centrum Nauki Kopernik', 'id': 'C13'}, {'name': 'Stadion Narodowy', 'id': 'C14'}, {'name': 'Dworzec Wileński', 'id': 'C15'}, {'name': 'Szwedzka', 'id': 'C16'}, {'name': 'Targówek Mieszkaniowy', 'id': 'C17'}, {'name': 'Trocka', 'id': 'C18'}], [{'name': 'Księcia Janusza', 'id': 'C6'}, {'name': 'Młynów', 'id': 'C7'}, {'name': 'Płocka', 'id': 'C8'}, {'name': 'Rondo Daszyńskiego', 'id': 'C9'}]]}], 'reason': 'zdarzenia', 'replacement_service': {'by_extension': True, 'exists': True, 'name': None}}
