from metro_stations import Station, M1, M2

def pattern(*args, **kwargs):
    print(args, kwargs)
    def inner(func):
        print(args)
        print(func(3))
        return func
    return inner

@pattern('loop', [2, 3])
def loop(arg):
    a = 1 + 3 + arg
    return a

def loop(start, end):
    pass