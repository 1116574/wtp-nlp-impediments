import logging
import json, html, argparse
from datetime import datetime

import requests
from rss_parser import Parser

from wtp_nlp.nlp.language_processor import language_processor
import wtp_nlp.utils.get_from_network
import wtp_nlp.utils.output
import wtp_nlp.nlp.highlihter


def maker(broken_html):
    """ This jerryrigged contrapciton is used for manually making tests """
    print('########')
    from bs4 import BeautifulSoup
    body = html.unescape(broken_html)
    soup = BeautifulSoup(body, 'html.parser')
    processed_html = [s for s in soup.strings]
    text = ' '.join(processed_html)
    print(text)
    print('======')
    # from rich.console import Console
    # console = Console()
    # console.print(language_processor(text))
    return text


def main(args = None):
    parser = argparse.ArgumentParser()

    input_src = parser.add_mutually_exclusive_group()
    input_src.add_argument('-n', '--network', help='Get alerts from RSS and mkuran (default)', action='store_true', default=True)  # masło maślane
    input_src.add_argument("-t", "--text", help="Pass alert text as an argument, skipping RSS")
    input_src.add_argument("-ht", "--html", help="Pass alert text in html as an argument, skipping RSS")
    input_src.add_argument("-f", "--file", help="Pass alert text in a file, skipping RSS")

    parser.add_argument("-o", "--out", help="choose output format: gtfs or json (default: json)", default='json')
    parser.add_argument("-of", "--out_file", help="filename for output", default=False)
    parser.add_argument("-ot", "--out_timestamp", help="timestamp the output", default=True)
    
    parser.add_argument("-dt", "--debug_tokenizer", help="run only tokenizer then quit", default=False, action='store_true')
    parser.add_argument("-dp", "--debug_pattern", help="run only tokenizer and pattern matcher then quit", default=False, action='store_true')
    parser.add_argument("-v", "--verbosity", help="set verbosity level", default=2, action='count')

    if not args:
        args = parser.parse_args()  # from command line
    # else: # args come from main(args), probably from test

    verbosity = (5 - args.verbosity) * 10
    logging.basicConfig(level=verbosity)
    logging.info('Started')

    logging.debug(args)

    # 1. Get data from network or file
    if args.text:
        data = args.text
    elif args.html:
        data = maker(args.html)
    elif args.file:
        with open(args.file, 'r') as f:
            data = f.read()
    elif args.network:
        data = wtp_nlp.utils.get_from_network.get_impidements()

    # print(data)
    if data is None:
        logging.info('No data/No impediments are taking place')
        quit()
    else:
        # Quickfix - add a leading garbage character - helps matching M1/M2
        data = 'G ' + data

    # 1.5. Check for debug flags
    if args.debug_tokenizer:
        from rich import console
        con = console.Console()
        con.print(wtp_nlp.nlp.highlihter.tokenizer(data))
        quit()

    # 2. Process data
    processed = language_processor(data)
    logging.debug(f'language_processor returned: {processed}')
    # 2.5 Check for debug flags
    if args.debug_pattern:
        from rich import console
        con = console.Console()
        con.print(processed)
        quit()        

    # 3. Filter the results (discard NotImplemented)
    filtered = []
    # print('statuses')
    for pattern in processed:
        if pattern['processed_to'] != NotImplemented:
            # print(pattern)
            filtered.append(pattern)

    
    # 4. Generate timestamp, if requested
    if args.out_timestamp:
        timestamp = datetime.now().isoformat()
    else:
        timestamp = False

    # 5. Generate some kind of output, be it json or gtfs feed
    if args.out == 'json':
        logging.info('json:')
        # print(filtered)
        output = wtp_nlp.utils.output.generate_json(filtered, timestamp=timestamp)
    elif args.out == 'gtfs':
        logging.info('gtfs:')
        output = wtp_nlp.utils.output.generate_gtfs(filtered)

    # 6. Save (optional)
    if args.out_file:
        with open(args.out_file, 'w') as f:
            json.dump(output, f, indent=4)
    
    # The end.
    print(output)
    return output


    # print(__name__)


if __name__ == '__main__':
    main()