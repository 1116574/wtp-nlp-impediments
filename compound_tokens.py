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


def find_pattern(full_text: list, full_pattern: list) -> list:
    i = 0
    out = []
    for node in full_text:
        if matches(node, full_pattern[i]):
            # print('ye', i, node, pattern[i])
            out.append(node)
            i += 1
        else: 
            i = 0
            out = []

        if i >= len(full_pattern):
            i = 0
            # print('patter done', node)
            return out


def execute(text, patterns):
    for pattern in patterns:
        result = find_pattern(text, patterns[pattern])
        if result:
            print(pattern, result)

            import status
            if hasattr(status, pattern):
                print('calling status')
                exec_func = getattr(status, pattern)
                final = exec_func(result)
                print(final)
            else:
                print('Not implemented yet.')

        print('=====')

if __name__ == '__main__':
    # from external tokenizer
    # text = [15, tokens.Metro_Line('M2'), 1, tokens.Reduced_Service, 0, tokens.On, 8, Station('C6', 'Księcia Janusza', [], True), 1, tokens.Between, 0, Station('C17', 'Targówek Mieszkaniowy', ['Targówek'], True)]
    text = [13, tokens.Metro_Line('M1'), 11, tokens.Loop, 1, Station('A1', 'Kabaty', [], True), 1, tokens.Between, 1, Station('A20', 'Słodowiec', [], True), 1, tokens.Between, 1, Station('A1', 'Kabaty', [], True), 0]
    patterns = get_patterns()
    execute(text, patterns)
    pass

