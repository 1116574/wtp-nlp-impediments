import json, html

from highlihter import tokenizer

import requests
from rss_parser import Parser

def language_processor(text):
    token_collection = tokenizer(text)
    results = token_collection

    # do stuff

    return results


print(language_processor('Z przyczyn technicznych w rejonie stacji Dworzec Gdański > Kabaty występują utrudnienia w kursowaniu linii M1. Możliwe opóźnienia na linii ok 10-12 min.'))


if __name__ == '__main__':
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
                    print(language_processor(entry.body))

