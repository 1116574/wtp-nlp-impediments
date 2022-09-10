from multiprocessing import current_process
import wtp_nlp
from wtp_nlp.data.metro_stations import Station
from wtp_nlp.data.status import Disabled, Ok, Degraded, Degraded_Segment, Degraded_Line, Loop, Double_Loop, Facilities, Replacement_Service, Reason

import logging, copy

from wtp_nlp.data.tokens import Metro_Line, TOKEN_M1, TOKEN_M2
from wtp_nlp.data.metro_stations import M1, M2


def _infere_line(station: Station) -> Metro_Line:
    if station in M1:
        return TOKEN_M1
    if station in M2:
        return TOKEN_M2


def _create_segment(segment: list[Station]) -> list:
    output = []
    for station in segment:
        output.append({
            "name": station.name,
            "id": station.id,
            "gtfs_id": station.gtfs_id
        })

    return output


def generate_gtfs():
    pass


def json_stub(timestamp):
    # This whole module should be better arranged, but mvp
    return {"timestamp": timestamp, "conditions": None}

def generate_json(parsed, timestamp=False):
    logger = logging.getLogger('output')
    logger.debug(f'json:recieved: {parsed}')

    condition = {
        "status": None,
        "line": None,
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

        current_condition = copy.copy(condition)
        if status is Loop:

            current_condition["status"] = 'Loop'
            current_condition["line"] = str(_infere_line(data[0][0]))
            affected = _create_segment(data[0])
            current_condition["affected"] = affected
            template["conditions"].append(current_condition)


        elif status is Double_Loop:
            for leg in data:
                if leg == []:
                    continue
                    # This is masking an underlying problem. FIXME (low priority)
                current_condition = copy.copy(condition)

                current_condition["status"] = 'Loop'
                current_condition["affected"] = []
                current_condition["line"] = str(_infere_line(leg[0]))

                affected = _create_segment(leg)

                current_condition["affected"] = affected
                template["conditions"].append(current_condition)
    

        elif status is Reason:
            template["reason"] = str(data[0])

        elif status is Replacement_Service:
            if data[0] == True:
                template["replacement_service"]["exists"] = True
            elif data[0] == 'by_extension':  # bad
                template["replacement_service"]["exists"] = True
                template["replacement_service"]["by_extension"] = True
            else:
                logger.debug(f'json:repl serv name: {data[0]}')
                template["replacement_service"]["exists"] = True
                template["replacement_service"]["name"] = data[0]  # bad coupling here, but whatev
    
        elif status is Facilities:
            logger.debug(f'json:facilities: {data}')
            current_condition = copy.copy(condition)
            current_condition["status"] = 'Facilities'
            current_condition["affected"] = [str(entry) for entry in data]
            template["conditions"].append(current_condition)

        elif status is Degraded_Segment:
            logger.debug(f'json:degraded_segment: {data}')
            current_condition = copy.copy(condition)
            current_condition["status"] = 'Degraded_Segment'
            current_condition["affected"] = _create_segment(data[0])
            current_condition["line"] = str(_infere_line(data[0][0]))
            template["conditions"].append(current_condition)

        elif status is Degraded_Line:
            logger.debug(f'json:degraded: {data}')
            current_condition = copy.copy(condition)
            current_condition["status"] = 'Degraded_Line'
            current_condition["affected"] = [str(entry) for entry in data]
            
            if len(data) == 1:
                current_condition["line"] = str(data[0])
            else:
                current_condition["line"] = 'multiple'

            template["conditions"].append(current_condition)

        elif status is Degraded:  # TODO FIXME Legacy code for closed stations
            logger.debug(f'json:degraded: {data}')
            current_condition = copy.copy(condition)
            current_condition["status"] = 'Degraded'
            current_condition["affected"] = [str(entry) for entry in data]
            template["conditions"].append(current_condition)

        elif status is Disabled:
            current_condition["status"] = 'Disabled'
            current_condition["affected"] = [str(entry) for entry in data]
            template["conditions"].append(current_condition)

    if timestamp:
        template["timestamp"] = timestamp

    # Check for duplicate conditions. This is a dirty fix to an underlying problem TODO: Fix properly
    if len(template["conditions"]) > 1:
        for n, cond in enumerate(template["conditions"]):
            for cond2 in template["conditions"][n+1:]:
                if cond == cond2:
                    template["conditions"].pop(n)

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