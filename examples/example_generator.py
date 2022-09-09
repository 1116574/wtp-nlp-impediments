# Generate outputs from ../tests/history.json

import json

# this is retarded
import sys
sys.path.append('..')
from wtp_nlp import __main__ as main

with open('../tests/history.json', 'r', encoding='UTF-8') as f:
    history = json.load(f)

class Args:
    def __init__(self, html, out_file) -> None:
        self.html = html
        self.text = None
        self.out = 'json'
        self.debug_tokenizer = False
        self.debug_pattern = False
        self.out_file = out_file
        self.verbosity = 3
        self.out_timestamp = False
        self.include = True

for n, entry in enumerate(history):
    main.main(Args(entry['body'], f'test-{n}.json'))