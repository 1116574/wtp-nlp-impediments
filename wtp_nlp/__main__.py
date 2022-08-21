import logging
import json, html, argparse

import requests
from rss_parser import Parser

from wtp_nlp.nlp.language_processor import language_processor
import wtp_nlp.utils.get_from_network
import wtp_nlp.utils.gtfs_gen


def maker():
    """ This jerryrigged contrapciton is used for manually making tests """
    print('########')
    from bs4 import BeautifulSoup
    body = html.unescape("""<p><strong>08:41</strong></p><p><strong>Koniec utrudnie&#x144;. Trwa przywracanie rozk&#x142;adowej organizacji ruchu.</strong></p><p><strong>06:01</strong></p><p>Z przyczyn technicznych do odwo&#x142;ania wyst&#x119;puj&#x105; utrudnienia w kursowaniu poci&#x105;g&#xF3;w linii metra <strong>M2</strong> . Poci&#x105;gi mog&#x105; kursowa&#x107; ze zmniejszon&#x105; cz&#x119;stotliwo&#x15B;ci&#x105; . Linia kursuje w p&#x119;tli <strong>Trocka &#x2013; Rondo Daszy&#x144;skiego &#x2013; Trocka</strong> . Zamkni&#x119;te dla ruchu zostaj&#x105; stacje metra linii <strong>M2</strong> : Ksi&#x119;cia Janusza , M&#x142;yn&#xF3;w i P&#x142;ocka . Trwa uruchamianie autobusowej linii <strong>Z </strong>kursuj&#x105;cej na trasie : <strong>Ksi&#x119;cia Janusza &#x2013; G&#xF3;rczewska &#x2013; P&#x142;ocka &#x2013; Kasprzaka &#x2013; Rondo Daszy&#x144;skiego</strong> &#x2013; <strong>Kasprzaka &#x2013; P&#x142;ocka &#x2013; G&#xF3;rczewska &#x2013; Ksi&#x119;cia Janusza .</strong> Prosimy o korzystanie z autobusowej linii <strong>109</strong> obs&#x142;uguj&#x105;cej przystanki w zespo&#x142;ach przystankowych <strong>Rondo Daszy&#x144;skiego i Metro Ksi&#x119;cia Janusza</strong> . Mo&#x17C;na r&#xF3;wnie&#x17C; korzysta&#x107; z tramwajowej linii <strong>10</strong> obs&#x142;uguj&#x105;cej przystanki w zespo&#x142;ach przystankowych <strong>Rondo Daszy&#x144;skiego i Metro P&#x142;ocka.</strong></p><p><strong>Przepraszamy za utrudnienia.</strong></p>""")
    soup = BeautifulSoup(body, 'html.parser')
    processed_html = [s for s in soup.strings]
    text = ' '.join(processed_html)
    print(text)
    print('======')
    from rich.console import Console
    console = Console()
    console.print(language_processor(text))


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Started')

    parser = argparse.ArgumentParser()

    input_src = parser.add_mutually_exclusive_group()
    input_src.add_argument('-n', '--network', help='Get alerts from RSS and mkuran (default)', action='store_true', default=True)  # masło maślane
    input_src.add_argument("-t", "--text", help="Pass alert text as an argument, skipping RSS")
    input_src.add_argument("-f", "--file", help="Pass alert text in a file, skipping RSS")

    parser.add_argument("-o", "--out", help=" choose output format: gtfs or json (default: json)", default='json')

    args = parser.parse_args()
    logging.debug(args)

    # 1. Get data from network or file
    if args.text:
        data = args.text
    elif args.file:
        with open(args.file, 'r') as f:
            data = f.read()
    elif args.network:
        data = wtp_nlp.utils.get_from_network.get_impidements()

    # print(data)
    if data is None:
        print('No data/No impediments are taking place')
        quit()

    # 2. Process data
    processed = language_processor(data)
    print('Finished with: ', processed)

    # 3. Filter the results (discard NotImplemented)
    print('statuses')
    for pattern in processed:
        if pattern['processed_to'] != NotImplemented:
            print(pattern)
        

    # 4. Generate some kind of output, be it json or gtfs feed
    print(__name__)


if __name__ == '__main__':
    main()