from wtp_nlp.data.tokens import TOKEN_M1, TOKEN_M2
from .metro_stations import Station, M1, M2
from .metro_stations import A14, C11


def _service_between(start: Station, end: Station, sort=True) -> list[Station]:
    if start in M1 and end in M1:
        metro = M1
    elif start in M2 and end in M2:
        metro = M2
    elif start in M1 and end in M2 and start.id == 'A23':  # (start) Świętokrzyska on M1 but should be on M2
        metro = M2
        start = C11
    elif start in M2 and end in M1 and start.id == 'C11':  # (start) Świętokrzyska on M2 but should be on M1
        metro = M1
        start = A14
    elif start in M1 and end in M2 and end.id == 'A23':  # (end) Świętokrzyska on M1 but should be on M2
        metro = M2
        end = C11
    elif start in M2 and end in M1 and end.id == 'C11':  # (end) Świętokrzyska on M2 but should be on M1
        metro = M1
        end = A14
    else:
        raise ValueError(f'Cant establish metro line of: {start}, {end}')

    start_index = metro.index(start)
    end_index = metro.index(end)


    loop = metro[start_index:end_index+1]
    if loop == []:
        # reverse the order lmao
        loop = _service_between(end, start)
        if sort:
            loop.sort(key=lambda station: int(station.id[1:]))
        return loop
    else:
        if sort:
            loop.sort(key=lambda station: int(station.id[1:]))
        return loop

class Status:
    pass

class Ok(Status):
    pass

# class Degraded(Status):
#     pass

class Station_Closed(Status):
    pass

class Degraded_Segment(Status):
    pass

class Degraded_Line(Status):
    pass

class Disabled(Status):
    pass

class Loop(Status):
    pass

class Double_Loop(Status):
    pass

class Facilities(Status):
    pass

class Replacement_Service(Status):
    pass

class Reason(Status):
    pass

# yea its not split according to concern, not semantic and all that
# but i just want it to work and its temporary

def loop(pattern):
    start = pattern[2]
    end = pattern[6]
    return Loop, _service_between(start, end)


def loop_1(pattern):
    start = pattern[4]
    end = pattern[8]
    return Loop, _service_between(start, end)


def loop_ext(pattern):
    return loop(pattern)


def loop_ext_1(pattern):
    return loop_1(pattern)


def reduced_service(pattern):
    start = pattern[6]
    end = pattern[10]
    return Degraded_Segment, _service_between(start, end)


def reduced_service_1(pattern):
    start = pattern[4]
    end = pattern[8]
    return Degraded_Segment, _service_between(start, end)    


def reduced_service_2(pattern):
    return Degraded_Line, pattern[2]


def reduced_service_3(pattern):
    return Degraded_Line, pattern[0]


def reduced_service_4(pattern):
    return Degraded_Line, pattern[2], pattern[6]


def reduced_service_5(pattern):
    return Degraded_Segment, _service_between(pattern[2], pattern[6])


def shortened_service(pattern):
    return Loop, _service_between(pattern[4], pattern[8])


def loop_double(pattern):
    # [Loop_Double, 4, 'relation', 6, And, 6, 'relation']
    return Double_Loop, _service_between(pattern[2], pattern[6]), _service_between(pattern[10], pattern[14])


def loop_double_1(pattern):
    return Double_Loop, _service_between(pattern[4], pattern[8]), _service_between(pattern[12], pattern[16])


def loop_double_2(pattern):
    return loop_double_1(pattern)


def loop_double_but_fuck_you(pattern):
    return loop_double(pattern)


def loop_run(pattern):
    return Loop, _service_between(pattern[6], pattern[10])

def partly_down(pattern):  ## AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    # [Not_Functioning_Service, 32, 'relation']
    excluded = _service_between(pattern[2], pattern[6])
    if pattern[2] in M1:
        metro = M1
    elif pattern[2] in M2:
        metro = M2
    # service = [station for station in metro if station not in excluded]
    out1 = []
    out2 = []
    current = out1
    for station in metro:
        if station not in excluded:
            current.append(station)
        else:
            current = out2
            continue

    return Double_Loop, out1, out2


def partly_down_1(pattern):
    return partly_down(['dummy', 'dummy', pattern[4], 'dummy', 'dummy', 'dummy', pattern[8]])


def partly_down_2(pattern):
    return partly_down(['dummy', 'dummy', pattern[6], 'dummy', 'dummy', 'dummy', pattern[10]])


def partly_down_3(pattern):
    return Degraded_Line, pattern[2]


def partly_down_4(pattern):
    return partly_down(['dummy', 'dummy', pattern[4], 'dummy', 'dummy', 'dummy', pattern[8]])


def shortened_service(pattern):
    return Loop, _service_between(pattern[4], pattern[8])


def shortened_service_1(pattern):
    return Loop, _service_between(pattern[2], pattern[6])


def shortened_service_2(pattern):
    return Loop, _service_between(pattern[0], pattern[4])


def facility_offline(pattern):
    return Facilities, pattern[4]


def facility_offline_1(pattern):
    return Facilities, pattern[2]


def facility_offline_2(pattern):
    return Facilities, pattern[0]


def facility_offline_3(pattern):
    return Facilities, pattern[4]


def service_on(pattern):
    return Loop, _service_between(pattern[5], pattern[9])


def service_on_double(pattern):
    return Double_Loop, _service_between(pattern[5], pattern[9]), _service_between(pattern[13], pattern[17])


def service_on_reason(pattern):
    return Loop, _service_between(pattern[5], pattern[9])

def service_on_reason_double(pattern):
    return Double_Loop, _service_between(pattern[5], pattern[9]), _service_between(pattern[13], pattern[17])

def station_closed(pattern):
    return Station_Closed, pattern[2]

def skipping(pattern):
    pass  # TODO: Implement.
    return Double_Loop, _service_between(pattern[2], pattern[10]), _service_between(pattern[6], pattern[10])

def all_down(pattern):
    return Disabled, TOKEN_M1, TOKEN_M2

def reason(pattern):
    return Reason, pattern[0]


def replacement_service(pattern):
    return Replacement_Service, True

def replacement_service_1(pattern):
    return Replacement_Service, pattern[0].repl_name

def replacement_service_by_extension(pattern):
    return Replacement_Service, 'by_extension'
