from wtp_nlp.data.metro_stations import Station, M1, M2

def _service_between(start, end):
    if start in M1:
        metro = M1
    elif start in M2:
        metro = M2

    start = metro.index(start)
    end = metro.index(end)

    return metro[start:end+1]


# yea its not split according to concern, not semantic and all that
# but i just want it to work and its temporary

def loop(pattern):
    start = pattern[2]
    end = pattern[6]
    return _service_between(start, end)

def loop_ext(pattern):
    return loop(pattern)

def reduced_service(pattern):
    start = pattern[6]
    end = pattern[10]
    return _service_between(start, end)

def reduced_service_1(pattern):
    start = pattern[4]
    end = pattern[8]
    return _service_between(start, end)    

def reduced_service_2(pattern):
    return f'Degraded service on {pattern[2]}' 


def shortened_service(pattern):
    pass

def loop_double(pattern):
    # [Loop_Double, 4, 'relation', 6, And, 6, 'relation']
    print(pattern)
    return [*_service_between(pattern[2], pattern[6]), *_service_between(pattern[8], pattern[12])]

def partly_down(pattern):
    # [Not_Functioning_Service, 12, 'relation']
    excluded = _service_between(pattern[2], pattern[6])
    if pattern[2] in M1:
        metro = M1
    elif pattern[2] in M2:
        metro = M2
    service = [station for station in metro if station not in excluded]
    return service