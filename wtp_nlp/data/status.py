from wtp_nlp.data.metro_stations import Station, M1, M2
from wtp_nlp.data.tokens import Loop_Double

def _service_between(start, end):
    if start in M1:
        metro = M1
    elif start in M2:
        metro = M2

    start_index = metro.index(start)
    end_index = metro.index(end)

    loop = metro[start_index:end_index+1]
    if loop == []:
        # reverse the order lmao
        return _service_between(end, start)
    else:
        return loop

class Status:
    pass

class Ok(Status):
    pass

class Degraded(Status):
    pass

class Loop(Status):
    pass

class Double_Loop(Status):
    pass

class Facilities(Status):
    pass

# yea its not split according to concern, not semantic and all that
# but i just want it to work and its temporary

def loop(pattern):
    start = pattern[2]
    end = pattern[6]
    return Loop, _service_between(start, end)

def loop_ext(pattern):
    return Loop, loop(pattern)

def reduced_service(pattern):
    start = pattern[6]
    end = pattern[10]
    return Degraded, _service_between(start, end)


def reduced_service_1(pattern):
    start = pattern[4]
    end = pattern[8]
    return Degraded, _service_between(start, end)    


def reduced_service_2(pattern):
    return Degraded, f'Degraded service on {pattern[2]}' 


def shortened_service(pattern):
    return Loop, _service_between(pattern[4], pattern[8])


def loop_double(pattern):
    # [Loop_Double, 4, 'relation', 6, And, 6, 'relation']
    print(pattern)
    return Loop_Double, [*_service_between(pattern[2], pattern[6]), *_service_between(pattern[8], pattern[12])]


def partly_down(pattern):
    # [Not_Functioning_Service, 12, 'relation']
    excluded = _service_between(pattern[2], pattern[6])
    if pattern[2] in M1:
        metro = M1
    elif pattern[2] in M2:
        metro = M2
    service = [station for station in metro if station not in excluded]
    return Double_Loop, service


def facility_offline(pattern):
    return Facilities, pattern[4]


def facility_offline_1(pattern):
    return Facilities, pattern[2]


def facility_offline_2(pattern):
    return Facilities, pattern[0]


def service_on(pattern):
    return Loop, _service_between(pattern[4], pattern[8])
