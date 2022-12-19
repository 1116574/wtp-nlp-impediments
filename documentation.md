# Documentation
## General format
```json
{
    "conditions": [
        {
            "status": "Degraded_Line",
            "line": "M1",
            "affected": [
                {
                    "id": "A9",
                    "name": "Station name",
                    "gtfs_id": "9999m"
                },
                {
                    "id": "A8",
                    "name": "Station name",
                    "gtfs_id": "9999m"
                }, ...and more
            ]
        },
        {
            "status": "Loop",
            "line": "M1",
            "affected": [
                {
                    "id": "A9",
                    "name": "Station name",
                    "gtfs_id": "9999m"
                },
                {
                    "id": "A8",
                    "name": "Station name",
                    "gtfs_id": "9999m"
                },
                {
                    "id": "A7",
                    "name": "Station name",
                    "gtfs_id": "9999m"
                }
            ]
        }, 
        ...there is no limit to amount of conditions, but Loops are usually most important so I suggest implementing them first
    ],
    "reason": "incident|technical|luggage|terrorism",
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

--------
### `Loop`
Service operates in a loop, like when last 3 stations are offline.

`affected` will be a list of currently operating stations eg. `[A, B, C]`.

`line` will be the line of the first station, either `M1` or `M2`.

note: order is guaranteed, so `[A, C, B]` is impossible, but the direction of ordering isn't. `[C, B, A]` is valid.  # todo: check this behaviour.

--------

### `Facilities`
Some facilities such as elevators or exits dont work.

`affected` will be station object that is experiencing difficultuies.

No `line` is provided for this status.

--------

### `Degraded_Segment`
There are (possibly undefinied) delays between stations, there are less trains than usual (reduced frequency), trains stop for longer then normal, or an otherwise condition that degrades the service, **but doesnt stop it completely**

`affected` will be a list of stops that service is degraded on.

`line` will be the line of the first station, either `M1` or `M2`.

--------
### `Degraded_Line`
A line (as a whole) is experiencing some difficulties.

`affected` will be a list of strings denoting the metro line (M1 or M2) that is experiencing difficulties.

`line` will be either `M1`, `M2` or `multiple` if there are multiple lines having trouble, eg.
```json
{
    "status": "Degraded_Line",
    "line": "multiple",
    "affected": ["M1", "M2"]
}
```
or
```json
{
    "status": "Degraded_Line",
    "line": "M1",
    "affected": ["M1"]
}
```

--------

### `Disabled`
Whole network is down, or more probably a bug arose. Since this is so infrequent its hard to test for. I suggest to ignore this if any other condition is available, like `Loop` or one of `Degraded_*` variants.

--------

### `Station_Closed`
Used for closed station. In future it might return multiple stations in a list

`affected` is the closed station object.

`line` is inferred from station.

--------


## Metro station object
```json
{
    "id": "A12",
    "name": "Wilanowska",
    "gtfs_id": "3009m"
}
```