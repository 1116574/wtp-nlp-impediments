import wtp_nlp
from wtp_nlp.data.status import Ok, Degraded, Loop, Double_Loop, Facilities, Replacement_Service, Reason

import logging

def generate_gtfs():
    pass


def generate_json(parsed):
    logger = logging.getLogger('output')
    logger.debug(f'json:recieved: {parsed}')

    template = {
        "status": None,
        "affected": None,
        "reason": None,
        "replacement_service": {
            "exists": False,
            "name": None,
            "by_extension": False
        }
    }

    current = template
    for entry in parsed:
        status = entry['processed_to'][0]  # status.Reason, status.Loop  etc.
        data = entry['processed_to'][1:]

        logger.debug(f'json:entry: {status} {data}')

        if status is Loop:
            current["status"] = 'Loop'
            affected = []
            for station in data[0]:
                affected.append({
                    "name": station.name,
                    "id": station.id,
                })
            current["affected"] = affected

        if status is Double_Loop:
            current["status"] = 'Double_Loop'
            current["affected"] = []
            for leg in data:
                affected = []
                for station in leg:
                    affected.append({
                        "name": station.name,
                        "id": station.id,
                    })
                current["affected"].append(affected)

        if status is Reason:
            current["reason"] = str(data[0])

        if status is Replacement_Service:
            if data == True:
                current["replacement_service"]["exists"] = True
            elif data == 'by_extension':  # bad
                current["replacement_service"]["exists"] = True
                current["replacement_service"]["by_extension"] = True
            else:
                logger.debug(f'json:repl serv name: {data[0]}')
                current["replacement_service"]["exists"] = True
                current["replacement_service"]["name"] = data[0]  # bad coupling here, but whatev
    
        if status is Facilities:
            pass
    
        if status is Degraded:
            pass

    pass

    return current

    # (Loop, ...), (Replacement_Service, ...)
    {
        "status": "Loop",
        "affected": ["Młociny", "...", "Wilanowska"],
        "reason": "[z powodu:] awari",
        "replacement_service": True,
        "replacement_service_name": None
    }

    # (Loop, ...), (Replacement_Service, ...), (Facilities, ...)
    {
        "status": "Loop",
        "affected": ["Młociny", "...", "Wilanowska"],
        "reason": "[z powodu:] awari",
        "replacement_service": True,
        "replacement_service_name": None
    }

    # (Loop, ...), (Degraded, ...), (Facilities, ...)
    {
        "status": "confused",
        "affected": None,
        "reason": None,
        "replacement_service": None,
        "replacement_service_name": None
    }

    {
        "interpreted": "first entry, or the one we are most sure about",
        "details": ["all other", "entries", "?"]
    }