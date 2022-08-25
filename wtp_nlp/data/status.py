from .metro_stations import Station, M1, M2


def _service_between(start: Station, end: Station, sort=True) -> list[Station]:
    if start in M1:
        metro = M1
    elif start in M2:
        metro = M2

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

class Degraded(Status):
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
    return Degraded, _service_between(start, end)


def reduced_service_1(pattern):
    start = pattern[4]
    end = pattern[8]
    return Degraded, _service_between(start, end)    


def reduced_service_2(pattern):
    return Degraded, pattern[2]


def reduced_service_3(pattern):
    return Degraded, pattern[0]


def shortened_service(pattern):
    return Loop, _service_between(pattern[4], pattern[8])


def loop_double(pattern):
    # [Loop_Double, 4, 'relation', 6, And, 6, 'relation']
    # print(pattern)
    return Double_Loop, _service_between(pattern[2], pattern[6]), _service_between(pattern[10], pattern[14])


def loop_double_1(pattern):
    return Double_Loop, _service_between(pattern[4], pattern[8]), _service_between(pattern[12], pattern[16])


def partly_down(pattern):
    # [Not_Functioning_Service, 12, 'relation']
    excluded = _service_between(pattern[2], pattern[6])
    if pattern[2] in M1:
        metro = M1
    elif pattern[2] in M2:
        metro = M2
    service = [station for station in metro if station not in excluded]
    return Double_Loop, service


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
    return Loop, _service_between(pattern[4], pattern[8])


def service_on_double(pattern):
    return Double_Loop, _service_between(pattern[4], pattern[8]), _service_between(pattern[12], pattern[16])


def service_on_reason(pattern):
    return Loop, _service_between(pattern[4], pattern[8])

def service_on_reason_double(pattern):
    return Double_Loop, _service_between(pattern[4], pattern[8]), _service_between(pattern[12], pattern[16])

def station_closed(pattern):
    return Degraded, pattern[2]


def reason(pattern):
    return Reason, pattern[0]


def replacement_service(pattern):
    return Replacement_Service, True

def replacement_service_1(pattern):
    return Replacement_Service, pattern[0].repl_name

def replacement_service_by_extension(pattern):
    return Replacement_Service, 'by_extension'