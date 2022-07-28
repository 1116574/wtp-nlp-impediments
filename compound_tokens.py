'''[
    15,
    < M2 >, 
    1, 
    <class 'tokens.Reduced_Service'>, 
    0, 
    <class 'tokens.On'>, 
    8, 
    < Księcia Janusza >, 
    1, 
    <class 'tokens.Between'>, 
    1, 
    < Targówek Mieszkaniowy >, 
    1
]'''

from metro_stations import Station 
import tokens


def matches(text, pattern):
    """
    Checks if given text fits the pattern.
    An instance of metro_station will match Statin, and a class
    of Reduced_Service will match another class of same name
    """
    '''
    5, 8
    Station(...), Station
    '''

    # (5, 8); (3, 11); (9, 3)
    if type(text) == int and type(pattern) == int:
        if text < pattern:
            return True  # (5, 8); (3, 11)
        else:
            return False  # (9, 3)

    # (8, Station); (Metro_Line, 11)
    if (type(text) == int and type(pattern) != int) or (type(text) != int and type(pattern) == int):
        return False


    # Both are classes or a class+instance
    # First, check if instance
    if isinstance(text, pattern):
        return True
    
    # class+class
    if text is pattern:
        return True

# from external tokenizer
text = [15, tokens.Metro_Line('M2'), 1, tokens.Reduced_Service, 0, tokens.On, 8, Station('C6', 'Księcia Janusza', [], True), 1, tokens.Between, 0, Station('C17', 'Targówek Mieszkaniowy', ['Targówek'], True)]

# format: classes are tokens and stations objects,
#  between which are numbers representing maxiumm distance.
pattern = [Station, 6, tokens.Between, 6, Station]
# to this pattern, a [Station, 1, tokens.Between, 5, Station], would match.
# a [Station, 9 ..] wouldn't match.

i = 0
for node in text:
    if i >= len(pattern):
        i = 0
        print('patter done', node)

    # print(type(node), '|', type(pattern[i]))
    if matches(node, pattern[i]):
        print('ye', i, node, pattern[i])
        i += 1
    else: 
        i = 0


    # for p_node in pattern:
    #     if type(p_node) == type(node):
    #         # a match!

    #         # Check if its a distance value
    #         if type(p_node) == int and node > p_node:
    #             # distance too great
    #             continue