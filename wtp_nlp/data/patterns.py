from wtp_nlp.data.metro_stations import Station
from wtp_nlp.data.tokens import *

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

    # TODO: some kind of meta patterns?

    # At the time it seemed like a good idea alright? Who could have guessed it would morph into this...

    patterns = {
        'relation': [Station, 6, Between, 6, Station],
        'relation_ext': [Station, 6, Between, 6, Station, 6, Between, 6, Station], # '_same-0' # there is currently no way to specify 'same as first index'
        'reason': [Reason, 10, On_Station, 10, Station],
        'loop': [Loop, 4, 'relation'],
        'loop_1': [Loop, 4, On, 4, 'relation'],
        'loop_ext': [Loop, 4, 'relation_ext'],
        'loop_ext_1': [Loop, 4, On, 4, 'relation_ext'],
        'loop_double': [Loop_Double, 4, 'relation', 6, And, 6, 'relation'],
        'loop_double_1': [Loop_Double, 4, On, 4, 'relation', 6, And, 6, 'relation'],
        'reduced_service': [Metro_Line, 10, Reduced_Service, 10, On, 10, 'relation'],
        'reduced_service_1': [Metro_Line, 10, On, 10, 'relation', Reduced_Service],
        'reduced_service_2': [Reduced_Service, 32, Metro_Line],
        'shortened_service': [Shortened_Service, 6, On, 6, 'relation'],
        'shortened_service_1': [Shortened_Service, 8, 'relation'],
        'shortened_service_2': ['relation', 8, Shortened_Service],
        'partly_down': [Not_Functioning_Service, 12, 'relation'],
        'facility_offline': [Not_Functioning_Facility, 32, Metro_Line, 8, Station],
        'facility_offline_1': [Not_Functioning_Facility, 24, Station],
        'facility_offline_2': [Station, 24, Not_Functioning_Facility],
        'facility_offline_3': [Not_Functioning_Facility, 8, On_Station, 8, Station],
        'service_on': [Metro_Line, 12, On, 6, 'relation'],
        'station_closed': [Not_Functioning_Station, 16, Station],

        # Special boolean-flag-like patterns (?)
        'replacement_service': [Replacement_Service],
        'replacement_service_1': [Metro_Replacement_Names],
        'replacement_service_by_extension': [Detour_By_Extension],
        'reason': [Reason],
    }

    new_patterns = patterns

    for p in patterns:
        # print(p)
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