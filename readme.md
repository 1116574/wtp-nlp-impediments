# wtp-impediments
This projects aims to process text data from alerts given out by Warsaw's public transport authority to a meaningful data used by routing systems.

# What?
Consider this:
```
16:42

Zakończenie utrudnień.

Z przyczyn technicznych od godz. 15:35 – wyłączenie ruchu pociągów i zamknięcie stacji.

Linia M1 – wyłączenie: Odcinek Metro Wilanowska – pl. Wilsona
Linia M2 – wyłączenie: Odcinek Ks. Janusza – Dw. Wileński

[...rest omitted for clarity...]
```
this program parses it into:  (TODO: give a working example)
```
{
    "conditions": [
        {
            "status": "Loop",
            "line": "M2",
            "affected": [
                {
                    "name": "Rondo Daszyńskiego",
                    "id": "C9",
                    "gtfs_id": "5040m"
                },
                [...rest omitted for clarity...]
                {
                    "name": "Trocka",
                    "id": "C18",
                    "gtfs_id": "1140m"
                }
            ]
        },
        {
            "status": "Degraded_Line",
            "line": "M2",
            "affected": [
                "M2"
            ]
        },
        {
            "status": "Loop",
            "line": "M1",
            "affected": [
                {
                    "name": "Wilanowska",
                    "id": "AA",
                    "gtfs_id": "XXXm"
                },
                [...rest omitted for clarity...]
                {
                    "name": "Plac Wilsona",
                    "id": "AA",
                    "gtfs_id": "XXXXm"
                }
            ]
        },
    ],
    "reason": "technicznych",
    "replacement_service": {
        "exists": true,
        "name": "linii Z",
        "by_extension": false
    },
}
```


