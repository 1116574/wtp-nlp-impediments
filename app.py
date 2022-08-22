from wtp_nlp.__main__ import main

from flask import Flask, request
from markupsafe import escape

class Args:
    def __init__(self, text, out) -> None:
        self.text = text
        self.out = out
        self.debug_tokenizer = False
        self.verbosity = 3


app = Flask(__name__)

@app.route('/<string:text>')
def hello(text):
    bruh = main(Args(escape(text), 'json'))
    # name = request.args.get("name", "World")
    return bruh