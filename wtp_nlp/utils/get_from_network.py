from wtp_nlp.nlp.language_processor import language_processor

import requests
from rss_parser import Parser
from rss_parser.models import RSSFeed


def _get_rss() -> RSSFeed:
    print('Calling wtp.waw.pl')
    rss_url = "https://www.wtp.waw.pl/feed/?post_type=impediment"
    xml = requests.get(rss_url)
    xml.raise_for_status()

    parser = Parser(xml=xml.content)
    return parser.parse()


def get_impidements(feed=_get_rss(), alerts=None):
    print('Looking for metro impedimets')
    for item in feed.feed:
        if any(x in item.title for x in ['M1', 'M2', 'Metro', 'Metra']):
            print('Found one, calling mkuran to get parsed data (TODO: Self hosted parsing):', item.title)
            # Now one should do some intensive html parsing bla bla bla, but why do that when you can use someone else's work?
            if not alerts:
                alerts = requests.get('http://mkuran.pl/gtfs/warsaw/alerts.json')
                alerts.raise_for_status()
                alerts = alerts.json()
            print("  Looking for the same impidement in mkuran's data")
            for entry in alerts['alerts']:
                if 'IMPEDIMENT' in entry["id"] and any(x in entry["routes"] for x in ['M1', 'M2', 'Metro', 'Metra']):
                    # We found an impediment ythats about metro, lets proceed
                    print('  Found:', entry["title"], ', passing to language-proccessor')
                    processed = language_processor(entry["body"])
                    print('  Finished with: ', processed)
                    return processed

