import json, html

import requests
from rss_parser import Parser

from wtp_nlp.nlp.language_processor import language_processor


def maker():
    """ Used for manually making tests """
    print('########')
    from bs4 import BeautifulSoup
    body = html.unescape("<div><div><h1><br><s>Zamkni&#x119;ta stacja &#x2013; Trocka.</s></h1></div></div><p><s>Z przyczyn technicznych zamkni&#x119;to stacj&#x119;<strong> Trocka</strong>. Poci&#x105;gi linii <strong>M2</strong> kursuj&#x105; na trasie skr&#xF3;conej: <strong>Metro Ksi&#x119;cia Janusza &#x2013; Targ&#xF3;wek Mieszkaniowy</strong>.</s></p><p style=\"background-color:#f4f736\"><s>UWAGA! W celu zapewnienia komunikacji na odcinku na kt&#xF3;rym wyst&#x119;puje zak&#x142;&#xF3;cenie, autobusy linii <strong>140, 199, 245, 256, 262 340, 738</strong> w obydwu kierunkach wykonuj&#x105; podjazd do stacji <strong>Targ&#xF3;wek Mieszkaniowy</strong>.</s></p><ul><li><s>Linie <strong>140, 199, 245, 256, 262, 340,738</strong> w obydwu kierunkach: &#x2026;Trocka &#x2013; <strong>METRO TROCKA 03</strong> &#x2013; Unicka &#x2013; Handlowa &#x2013; Ossowskiego &#x2013; <strong>METRO TARG&#xD3;WEK MIESZKANIOWY 02</strong> &#x2013; Barkoci&#x144;ska &#x2013; Myszkowska &#x2013; Handlowa &#x2013; Unicka &#x2013; Trocka&#x2026; do w&#x142;asnych tras.</s></li></ul><p><em>Przepraszamy za powsta&#x142;e utrudnienia.</em></p>")
    soup = BeautifulSoup(body, 'html.parser')
    processed_html = [s for s in soup.strings]
    text = ' '.join(processed_html)
    print(text)
    print('======')
    from rich.console import Console
    console = Console()
    console.print(language_processor(text))


def get_impidements():
    print('Calling wtp.waw.pl')
    rss_url = "https://www.wtp.waw.pl/feed/?post_type=impediment"
    xml = requests.get(rss_url)

    parser = Parser(xml=xml.content)
    feed = parser.parse()

    print('Looking for metro impedimets')
    for item in feed.feed:
        if any(x in item.title for x in ['M1', 'M2', 'Metro', 'Metra']):
            print('Found one, calling mkuran to get parsed data (TODO: Self hosted parsing):', item.title)
            # Now one should do some intensive html parsing bla bla bla, but why do that when you can use someone else's work?
            alerts = requests.get('http://mkuran.pl/gtfs/warsaw/alerts.json')
            alerts.raise_for_status()
            alerts = alerts.json()
            print("  Looking for the same impidement in mkuran's data")
            for entry in alerts['alerts']:
                if 'IMPEDIMENT' in entry.id and any(x in entry.routes for x in ['M1', 'M2', 'Metro', 'Metra']):
                    # We found an impediment ythats about metro, lets proceed
                    print('Found:', entry.title, ', passing to language-proccessor')
                    processed = language_processor(entry.body)
                    print(processed)
                    return processed


get_impidements()