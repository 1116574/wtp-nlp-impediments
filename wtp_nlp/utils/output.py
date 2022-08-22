from multiprocessing import current_process
import wtp_nlp
from wtp_nlp.data.status import Ok, Degraded, Loop, Double_Loop, Facilities, Replacement_Service, Reason

import logging, copy

def generate_gtfs():
    pass


def generate_json(parsed):
    logger = logging.getLogger('output')
    logger.debug(f'json:recieved: {parsed}')

    condition = {
        "status": None,
        "affected": None,
    }

    template = {
        "conditions": [],  # list of condition
        "reason": None,
        "replacement_service": {
            "exists": False,
            "name": None,
            "by_extension": False
        }
    }

    for entry in parsed:
        status = entry['processed_to'][0]  # status.Reason, status.Loop  etc.
        data = entry['processed_to'][1:]

        logger.debug(f'json:entry: {status} {data}')

        if status is Loop:
            current_condition = copy.copy(condition)

            current_condition["status"] = 'Loop'
            affected = []
            for station in data[0]:
                affected.append({
                    "name": station.name,
                    "id": station.id,
                })
            current_condition["affected"] = affected
            template["conditions"].append(current_condition)


        if status is Double_Loop:
            current_condition = copy.copy(condition)

            current_condition["status"] = 'Double_Loop'
            current_condition["affected"] = []
            for leg in data:
                affected = []
                for station in leg:
                    affected.append({
                        "name": station.name,
                        "id": station.id,
                    })
                current_condition["affected"].append(affected)
            template["conditions"].append(current_condition)
    

        if status is Reason:
            template["reason"] = str(data[0])

        if status is Replacement_Service:
            if data == True:
                template["replacement_service"]["exists"] = True
            elif data[0] == 'by_extension':  # bad
                template["replacement_service"]["exists"] = True
                template["replacement_service"]["by_extension"] = True
            else:
                logger.debug(f'json:repl serv name: {data[0]}')
                template["replacement_service"]["exists"] = True
                template["replacement_service"]["name"] = data[0]  # bad coupling here, but whatev
    
        if status is Facilities:
            logger.debug(f'json:facilities: {data}')
            current_condition = copy.copy(condition)
            current_condition["status"] = 'Facilities'
            current_condition["affected"] = str(data)
            template["conditions"].append(current_condition)

        if status is Degraded:
            logger.debug(f'json:degraded: {data}')
            current_condition = copy.copy(condition)
            current_condition["status"] = 'Degraded'
            current_condition["affected"] = str(data)
            template["conditions"].append(current_condition)

    pass

    return template

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