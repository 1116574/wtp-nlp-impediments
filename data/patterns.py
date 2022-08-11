from data.metro_stations import Station
from data.tokens import *

# format: classes are tokens and stations objects,
#  between which are numbers representing maxiumm distance.
# pattern = [Station, 6, Between, 6, Station]
# to this pattern, a [Station, 1, tokens.Between, 5, Station], would match.
# [Station, 9 ..] wouldn't match.


# @property
def get_patterns():
    """
    Extends (compiles?) patterns into a full machine readable version
    """

    patterns = {
        'relation': [Station, 6, Between, 6, Station],
        'relation_ext': [Station, 6, Between, 6, Station, 6, Between, 6, Station], # '_same-0' # there is currently no way to specify 'same as first index'
        'reason': [Reason, 10, On_Station, 10, Station],
        'loop': [Loop, 4, 'relation'],
        'loop_ext': [Loop, 4, 'relation_ext'],
        'loop_double': [Loop_Double, 4, 'relation', 6, And, 6, 'relation'],
        'reduced_service': [Metro_Line, 10, Reduced_Service, 10, On, 10, 'relation'],
        'shortened_service': [Shortened_Service, 6, On, 6, 'relation']
    }

    new_patterns = patterns

    for p in patterns:
        print(p)
        for i, item in enumerate(patterns[p]):
            if type(item) is str:
                new_patterns[p].pop(i)
                new_patterns[p][i:i] = patterns[item]

    return new_patterns


if __name__ == '__main__':
    from rich import print
    print(get_patterns())

# class Relation:
#     def __init__(self):
#         # an OR list of permitted patterns
#         self.patterns = [
#             [Station, 6, Between, 6, Station, 6, Between, 6, '_same-0'],
#             [Station, 6, Between, 6, Station],
#         ]
#         return self

# /\ This looks very complex, maybe in the next rewrite


# print(patterns)