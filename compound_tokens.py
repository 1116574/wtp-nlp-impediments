from data.metro_stations import Station 
import data.tokens as tokens
from data.patterns import get_patterns


def matches(text: any, pattern: any) -> bool:
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

#                                                       end_index, matched_pattern
def find_pattern(full_text: list, pattern: list) -> list[int, list]:
    '''
    Finds first `pattern` in `full_text`, returns the matching text and its index at which it was found in.
    '''
    i = 0
    out = []
    for n_indx, node in enumerate(full_text):
        if matches(node, pattern[i]):
            # print('ye', i, node, pattern[i])
            out.append(node)
            i += 1
        else: 
            i = 0
            out = []

        if i >= len(pattern):
            # print('sdsadgdfg', n_indx, full_text)
            i = 0
            # print('patter done', node)
            return n_indx, out

    return False, False


def find_all_patterns(full_text, pattern):
    '''
    Finds all occurences of a `pattern`
    '''
    index = 0
    out = []
    while True:
        index, occurence = find_pattern(full_text, pattern)
        if occurence:
            out.append(occurence)
            full_text = full_text[index:]
            # repeat
        else:
            # full_text exhausted, stop
            break

    return out


def execute(text, patterns):
    for pattern in patterns:
        results = find_all_patterns(text, patterns[pattern])
        if results:
            for result in results:
                import status
                if hasattr(status, pattern):
                    # print('calling status')
                    exec_func = getattr(status, pattern)
                    final = exec_func(result)
                    yield pattern, result, final
                else:
                    yield pattern, result, NotImplemented


if __name__ == '__main__':
    # from external tokenizer
    # text = [15, tokens.Metro_Line('M2'), 1, tokens.Reduced_Service, 0, tokens.On, 8, Station('C6', 'Księcia Janusza', [], True), 1, tokens.Between, 0, Station('C17', 'Targówek Mieszkaniowy', ['Targówek'], True)]
    text = [13, tokens.Metro_Line('M1'), 11, tokens.Loop, 1, Station('A1', 'Kabaty', [], True), 1, tokens.Between, 1, Station('A20', 'Słodowiec', [], True), 1, tokens.Between, 1, Station('A1', 'Kabaty', [], True), 0]
    patterns = get_patterns()
    for pattern_name, matching_text, final in execute(text, patterns):
        print(pattern_name, ':', matching_text, '->', final)
        print('====')
    pass

