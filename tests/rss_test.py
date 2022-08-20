import wtp_nlp
from wtp_nlp.utils import get_from_network

from rss_parser import Parser

rss_content = '''<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:atom="http://www.w3.org/2005/Atom"
	xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
	xmlns:slash="http://purl.org/rss/1.0/modules/slash/"
	>

<channel>
	<title>Warszawski Transport Publiczny</title>
	<atom:link href="https://www.wtp.waw.pl/feed/?post_type=impediment" rel="self" type="application/rss+xml" />
	<link>https://www.wtp.waw.pl</link>
	<description></description>
	<lastBuildDate>Fri, 19 Aug 2022 13:20:44 +0000</lastBuildDate>
	<language>pl-PL</language>
	<sy:updatePeriod>
	hourly	</sy:updatePeriod>
	<sy:updateFrequency>
	1	</sy:updateFrequency>
	<generator>https://wordpress.org/?v=5.8.2</generator>
	<item>
		<title>Utrudnienia w komunikacji: M1</title>
		<link>https://www.wtp.waw.pl/utrudnienia/2022/08/20/organizacja-komunikacji-w-zwiazku-z-impreza-pn-10-polmaraton-im-janusza-kusocinskiego/</link>
		
		<dc:creator><![CDATA[ZTM Warszawa]]></dc:creator>
		<pubDate>Sat, 20 Aug 2022 16:37:31 +0000</pubDate>
		<guid isPermaLink="false">https://www.wtp.waw.pl/?post_type=impediment&#038;p=87183</guid>

		<description><![CDATA[Organizacja komunikacji w związku z imprezą pn. „10. Półmaraton im. Janusza Kusocińskiego”]]></description>
		<content:encoded><![CDATA[Organizacja komunikacji w związku z imprezą pn. „10. Półmaraton im. Janusza Kusocińskiego”]]></content:encoded>
	</item>
</channel>
</rss>'''

alert_content = {
	"time": "is of no consequence",
	"alerts": [
		{
			"id": "A/IMPEDIMENT/87082",
			"routes": [
				"M1",
				"507",
			],
			"effect": "OTHER_EFFECT",
			"link": "",
			"title": "Problem na lini metra M1",
			"body": "Linia M1 kursuje w pętli Kabaty <-> Wilanowska",
			"htmlbody": ""
		}
	]
}

def test_get_impidements():
    parser = Parser(xml=rss_content)
    feed = parser.parse()
    processed = get_from_network.get_impidements(feed=feed, alerts=alert_content)
    assert processed[1]['processed_to'][0] == wtp_nlp.data.status.Loop
