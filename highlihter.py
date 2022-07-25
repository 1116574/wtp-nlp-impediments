import html, json
from bs4 import BeautifulSoup

from rich.console import Console

from metro_stations import M1
from tokens import TOKENS, Full_Stop

# body = "<p><strong>Z przyczyn technicznych wyst&#x119;puj&#x105; utrudnienia w kursowaniu metra linii M1. Metro kursuje w p&#x119;tli Metro Kabaty &#x2013; Metro S&#x142;odowiec &#x2013; Metro Kabaty.</strong></p><p><strong>Trwa uruchamianie komunikacji zast&#x119;pczej za metro.</strong></p><p><strong>Za utrudnienia przepraszamy.</strong></p>"
# body = html.unescape(body)

with open('history.json', 'r', encoding='utf-8') as f:
    history = json.load(f)

# body = html.unescape(history[20]['body'])  # 17  19 wejscie lol
body = html.unescape(history[3]['body'])
soup = BeautifulSoup(body, 'html.parser')
processed_html = [s for s in soup.strings]

completely_processed = []
for tag in processed_html:
    completely_processed += tag.split('.')

console = Console()

for body in completely_processed:
    print(body)

    for station in M1:
        if station.turn_around:
            token = f'[bold blue]{station}[/bold blue]'
        else:
            token = f'[bold green]{station}[/bold green]'

        
        body = body.replace(station.name, token)
        body = body.replace(station.name.upper(), token)
        body = body.replace(station.name.lower(), token)
        for form in station.forms:
            body = body.replace(form, token)
            body = body.replace(form.upper(), token)
            body = body.replace(form.lower(), token)


    for token in TOKENS:
        for word in token.raw:
            body = body.replace(word, f'[bold purple]{token}[/bold purple]')
            body = body.replace(word.capitalize(), f'[bold purple]{token}[/bold purple]')
    console.print('>>>', body, highlight=False)

