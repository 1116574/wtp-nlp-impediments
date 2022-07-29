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
from patterns import get_patterns


# from external tokenizer
text = [15, tokens.Metro_Line('M2'), 1, tokens.Reduced_Service, 0, tokens.On, 8, Station('C6', 'Księcia Janusza', [], True), 1, tokens.Between, 0, Station('C17', 'Targówek Mieszkaniowy', ['Targówek'], True)]


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


def find_pattern(text, pattern):
    i = 0
    out = []
    for node in text:
        if matches(node, pattern[i]):
            # print('ye', i, node, pattern[i])
            out.append(node)
            i += 1
        else: 
            i = 0
            out = []

        if i >= len(pattern):
            i = 0
            # print('patter done', node)
            return out


patterns = get_patterns()
for pattern in patterns:
    print(pattern)
    print(find_pattern(text, patterns[pattern]))

