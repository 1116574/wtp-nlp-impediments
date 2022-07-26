import html, json, re
from bs4 import BeautifulSoup

from rich.console import Console

from metro_stations import M1
from tokens import TOKENS, Full_Stop

# body = "<p><strong>Z przyczyn technicznych wyst&#x119;puj&#x105; utrudnienia w kursowaniu metra linii M1. Metro kursuje w p&#x119;tli Metro Kabaty &#x2013; Metro S&#x142;odowiec &#x2013; Metro Kabaty.</strong></p><p><strong>Trwa uruchamianie komunikacji zast&#x119;pczej za metro.</strong></p><p><strong>Za utrudnienia przepraszamy.</strong></p>"
# body = html.unescape(body)

with open('history.json', 'r', encoding='utf-8') as f:
    history = json.load(f)

# body = html.unescape(history[20]['body'])  # 17  19 wejscie lol
body = html.unescape(history[0]['body'])
soup = BeautifulSoup(body, 'html.parser')
processed_html = [s for s in soup.strings]

text = ' '.join(processed_html)

console = Console()
console.print(text)

semantic = [None] * len(text)

for station in M1:
    for name in station:
        index = text.find(name)
        if index >= 0:
            semantic[index] = station

print(semantic)