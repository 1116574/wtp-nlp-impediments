import html, json, re
from queue import Full
from bs4 import BeautifulSoup

from rich.console import Console

from data.metro_stations import M1, M2
from data.tokens import TOKENS, Full_Stop, And, Dummy


# https://stackoverflow.com/a/4665027/9366540
def _find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


def _distance_reduce(array: list):
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


def _abbrv(text: str):
    """ Replaces shorthands and periods with full word without periods """
    return text.replace(' pl. ', ' plac ').replace(' al. ', ' aleja ').replace(' os. ', ' osiedle ')


def tokenizer(text):
    semantic = [None] * len(text)

    # Normalize whitespace (double spaces -> single spaces)
    text = " ".join(text.split())

    # Detect sentences
    text = _abbrv(text)  # convert shorthands into full words, so `.` doesnt get mixed up
    results = _find_all(text, '.')
    for index in results:
        semantic[index] = Full_Stop

    # Detect 'and' ('i')
    results = _find_all(text, ' i ')
    for index in results:
        semantic[index] = And

    results = _find_all(text, ' oraz ')
    for index in results:
        semantic[index] = And

    # Metro stations
    for line in [M1, M2]:
        for station in line:
            for name in station:
                results = _find_all(text.lower(), name.lower())
                for index in results:
                    semantic[index] = station

                    # replace additional letters
                    for g in range(1, len(name)):
                        semantic[index+g] = Dummy

    # Important tokens - station shutdowns, loops
    for word in TOKENS:
        for name in word.raw:
            results = _find_all(text.lower(), name.lower())
            for index in results:
                semantic[index] = word

                # replace additional letters
                for g in range(1, len(name)):
                    semantic[index+g] = Dummy

    return _distance_reduce(semantic)

if __name__ == '__main__':
    reduced = tokenizer('Z przyczyn technicznych w rejonie stacji Dworzec Gdański > Kabaty występują utrudnienia w kursowaniu linii M1. Możliwe opóźnienia na linii ok 10-12 min.')
    # print(semantic)
    print('======')
    # print([x for x in semantic if x is not None])
    # reduced = _distance_reduce(semantic)
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