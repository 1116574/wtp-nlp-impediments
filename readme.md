# wtp-impediments
This projects aims to process text data from alerts given out by Warsaw's public transport authority to a meaningful data used by routing systems.

# Example
input:
```
W związku ze zdarzeniem na stacji metra Trocka, pociągi linii metra M2 kursują na trasie Bemowo – Targówek Mieszkaniowy.\n\nTrwa uruchamianie autobusowej komunikacji zastępczej.\n\nPrzepraszamy za utrudnienia."
```
<details>
    <summary>
    English translation
    </summary>
    <blockquote>
    Because of an incident at the Trocka metro station, trains on M2 metro line run on route Bemowo - Targówek Mieszkaniowy. Bus replacement service is being set up. Sorry for the inconvienice.
    </blockquote>
    If this translation seems weirdly worded - thats because it is. I tried to preserve as much orginal grammar and word sequence as possible, disregarding some shortcuts english would offer.
</details>

output (json):
```json
{
    "conditions": [
        {
            "status": "Loop",
            "line": "M2",
            "affected": [
                {
                    "name": "Bemowo",
                    "id": "C4",
                    "gtfs_id": "5034m"
                },
                {
                    "name": "Ulrychów",
                    "id": "C5",
                    "gtfs_id": "5032m"
                },
                {
                    "name": "Księcia Janusza",
                    "id": "C6",
                    "gtfs_id": "5030m"
                },
                {
                    "name": "Młynów",
                    "id": "C7",
                    "gtfs_id": "5028m"
                },
                {
                    "name": "Płocka",
                    "id": "C8",
                    "gtfs_id": "5005m"
                },
                {
                    "name": "Rondo Daszyńskiego",
                    "id": "C9",
                    "gtfs_id": "5040m"
                },
                {
                    "name": "Rondo ONZ",
                    "id": "C10",
                    "gtfs_id": "7088m"
                },
                {
                    "name": "Świętokrzyska",
                    "id": "C11",
                    "gtfs_id": "7014m"
                },
                {
                    "name": "Nowy Świat-Uniwersytet",
                    "id": "C12",
                    "gtfs_id": "7043m"
                },
                {
                    "name": "Centrum Nauki Kopernik",
                    "id": "C13",
                    "gtfs_id": "7079m"
                },
                {
                    "name": "Stadion Narodowy",
                    "id": "C14",
                    "gtfs_id": "1231m"
                },
                {
                    "name": "Dworzec Wileński",
                    "id": "C15",
                    "gtfs_id": "1003m"
                },
                {
                    "name": "Szwedzka",
                    "id": "C16",
                    "gtfs_id": "1526m"
                },
                {
                    "name": "Targówek Mieszkaniowy",
                    "id": "C17",
                    "gtfs_id": "1137m"
                }
            ]
        }
    ],
    "reason": "incident",
    "replacement_service": {
        "exists": true,
        "name": null,
        "by_extension": false
    },
    "timestamp": "2022-12-19T15:49:02.251714",
    "input": "G W związku ze zdarzeniem na stacji metra Trocka, pociągi linii metra M2 kursują na trasie Bemowo – Targówek Mieszkaniowy.\n\nTrwa uruchamianie autobusowej komunikacji zastępczej.\n\nPrzepraszamy za utrudnienia."
}
```

# What it did
The `affected` field is a list of sequential metro stops on which metro runs according to parsed service alert. In this case, last 3 stations arent on that list - Trocka, Zacisze, Szwedzka. Trains on this segment were stopped and dont run. If a central part of the line was to be closed, then you would see two `conditions` both with status loop, each covering appropriate leg of the remeaning line. See Warsaw metro diagram <a href="https://www.wtp.waw.pl/wp-content/uploads/sites/2/2020/02/szynowa.png">here, on their website (blue lines are metro)</a>, or see the in-repo <a href="diagram.png">technical diagram</a>.

# How it works
1. The network component pools RSS for metro service updates. If one is found, a call to mkuran's GTFS-RT service is made. Long story short, RSS does not include reuired data, and mkuran already went ahead and wrote html parser for the transport authority website<blockquote>
    Alternatively, you can include custom text with `-t` flag
</blockquote>


1. The text goes first to `highlighter.py` where first some processing is done, such as expanding abbriviations and normalization. Its then tokenized, according to the list in `data/tokens.py` as well as `data/reasons.py`. <blockquote>
    If you wish to see only the token data, specify `-dt` flag.
</blockquote>

2. Token list goes to `language_processor.py` where it is matched to known patterns specified in `compound_tokens.py`.
3. The resulting matches are then processed with functions from `status.py`
4. Those raw parsing results go to `output.py` which generates either json (default) or html. <blockquote>
    If you want to see unprocessed parsing data, specify `-dp` flag.
</blockquote>

# Documentation
[incomplete] For end consumer of json: <a href="documentation.md">*click*</a>

[more incomplete] For future me/other developer: <a href="developer_reference.md">*click*</a>
