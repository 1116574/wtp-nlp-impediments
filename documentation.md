# Documentation
## General format
```json
{
    "conditions": [
        {
            "status": "Degraded",
            "affected": "depends on status"
        },
        {
            "status": "Loop",
            "affected": [
                {
                    "id": "A9",
                    "name": "Station name"
                },
                {
                    "id": "A8",
                    "name": "Station name"
                },
                {
                    "id": "A7",
                    "name": "Station name"
                }
            ]
        }
    ],
    "reason": null|string,
    "replacement_service": {
        "exists": bool,
        "name": null|string,
        "by_extension": bool
    },
    "timestamp": "2022-08-25T21:47:50.467988 - iso formatted"
}
```

## `conditions` field
An Array of multible ongoing conditions, although usually one. A condition is, for example, station shutdown and subsequent split of services into 2 loops. Another condition might be an elevator failure, or reduced frequency.


## Allowed conditions
### `Loop`
Service operates in a loop, like when last 3 stations are offline.

`affected` will be a list of currently operating stations eg. `[A, B, C]`

note: order is guaranteed, so `[A, C, B]` is impossible, but the direction of ordering isn't. `[C, B, A]` is valid.  # todo: check this behaviour

### `Double_Loop`
2 distinct loops, when center section is offline - services are split into northern and southern loops.

`affected` will be a 2 len list of currently loops. eg. `[ [A, B, C], [F, G, H] ]`

### `Facilities`
Some facilities such as elevators or exits dont work.

`affected` will be station object that is experiencing difficultuies

### `Degraded`
There are (possibly undefinied) delays on the network or between stations, there are less trains than usual, eg. reduced frequency, or an otherwise condition that degrades the service, **but doesnt stop it completely**

`affected` will be either a list of stops that service is degraded on or a string denoting the metro line (M1 or M2) that is experiencing difficulties.

## Metro station object
```json
{
    "id": "A12",
    "name": "Wilanowska"
}
```