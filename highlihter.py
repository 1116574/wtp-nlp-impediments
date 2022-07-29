import html, json, re
from queue import Full
from bs4 import BeautifulSoup

from rich.console import Console

from metro_stations import M1, M2
from tokens import TOKENS, Full_Stop, And, Dummy

# body = "<p><strong>Z przyczyn technicznych wyst&#x119;puj&#x105; utrudnienia w kursowaniu metra linii M1. Metro kursuje w p&#x119;tli Metro Kabaty &#x2013; Metro S&#x142;odowiec &#x2013; Metro Kabaty.</strong></p><p><strong>Trwa uruchamianie komunikacji zast&#x119;pczej za metro.</strong></p><p><strong>Za utrudnienia przepraszamy.</strong></p>"
# body = html.unescape(body)


# https://stackoverflow.com/a/4665027/9366540
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


def distance_reduce(array: list):
    out = []
    count = 0
    for item in array:
        if item is None:
            count += 1
        elif item is Dummy:
            continue
        else:
            out.append(count)
            out.append(item)
            count = 0
    
    out.append(count)
    return out



with open('history.json', 'r', encoding='utf-8') as f:
    history = json.load(f)

# body = html.unescape(history[20]['body'])  # 17  19 wejscie lol
body = html.unescape(history[17]['body'])
body = '<p><strong><u>Trwa przywracanie podstawowej organizacji ruchu.</u></strong></p><p> Z powodu zdarzenia na stacji metra<strong> Centrum</strong> wyst&#x119;puj&#x105; utrudnienia w kursowaniu linii metra <strong>M1</strong>. Ruch odbywa si&#x119; w p&#x119;tlach: <strong>Kabaty &#x2013; Politechnika</strong> oraz <strong>Dw.Gda&#x144;ski &#x2013; M&#x142;ociny</strong>. </p><p> Na odcinku <strong>Metro Politechnika</strong> <strong>&#x2013; Dw. Gda&#x144;ski</strong> prosimy r&#xF3;wnie&#x17C; o korzystanie z tramwajowej linii <strong>4,15,18,35. </strong></p><p>Autobusy linii <strong>520</strong> kursuj&#x105; na wyd&#x142;u&#x17C;onej trasie <strong>Marysin&#x2026;..pl. Bankowy, Andersa &#x2013; pl. Wilsona.</strong></p><p> <strong>Przepraszamy za utrudnienia.</strong> </p>'
# 35 doesnt even have loop skull emoji
soup = BeautifulSoup(body, 'html.parser')
processed_html = [s for s in soup.strings]

text = ' '.join(processed_html)

# text = 'Linia metra MA12 kursuje w pętli Młocin-Centrum, wyłączone stacje: STP KABATY, Młociny, Plac Wilsona, Politechnika'

console = Console()
console.print(text)

semantic = [None] * len(text)

# Normalize whitespace (double spaces -> single spaces)
text = " ".join(text.split())

# Detect sentences
results = find_all(text, '.')  # TODO : recognize abbriviations, pl. -> plac; al. -> aleja; os. -> osiedle etc.
for index in results:
    semantic[index] = Full_Stop

# Detect 'and' ('i')
results = find_all(text, ' i ')
for index in results:
    semantic[index] = And

results = find_all(text, ' oraz ')
for index in results:
    semantic[index] = And

# Metro stations
for line in [M1, M2]:
    for station in line:
        for name in station:
            results = find_all(text.lower(), name.lower())
            for index in results:
                semantic[index] = station

                # replace additional letters
                for g in range(1, len(name)):
                    semantic[index+g] = Dummy

# Important tokens - station shutdowns, loops
for word in TOKENS:
    for name in word.raw:
        results = find_all(text.lower(), name.lower())
        for index in results:
            semantic[index] = word

            # replace additional letters
            for g in range(1, len(name)):
                semantic[index+g] = Dummy

# print(semantic)
print('======')
# print([x for x in semantic if x is not None])
reduced = distance_reduce(semantic)
# print(reduced)
print('======')
items = []
for obj in reduced:
    if obj is Full_Stop:
        print(items)
        items = []
    else:
        items.append(obj)

print(items)