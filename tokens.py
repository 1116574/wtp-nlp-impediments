from dataclasses import dataclass

@dataclass
class Token:
    """ Generic word token """
    raw: list
    name: str

    def __repr__(self):
        return f'< {self.name} >'

@dataclass
class Between(Token):
    """ Joins 2 or more stations """
    raw = ['↔', '–']
    name = '+'

@dataclass
class Replacement_Service(Token):
    raw = ['zastępcza linia', 'linia zastępcza', 'zastępcza', 'zastępczej']
    name = 'replacement'


@dataclass
class Not_Functioning(Token):
    raw = ['nie funkcjonują', 'nie kursują', 'wstrzymany', 'wstrzymane']
    name = 'not_functioning'

@dataclass
class Reduced_Service(Token):
    raw = ['zmniejszoną częstotliwością', 'kursuje na trasie skróconej', 'kursują na trasie skróconej', 'na trasie skróconej']
    name = 'reduced'

@dataclass
class Bus_service(Token):
    raw = ['autobusowa', 'autobusowej', 'autobus']
    name = 'bus'

@dataclass
class Loop(Token):
    raw = ['pętli', 'dwóch pętlach']
    name = 'bus'

@dataclass
class Metro_Replacement_Names(Token):
    raw = ['"ZA METRO"', 'ZA METRO', 'za "metro"']

@dataclass
class Full_Stop(Token):
    raw = ['.']

@dataclass
class On(Token):
    raw = ['na trasie', 'na odcinku']

@dataclass
class Recommended_Detour(Token):
    raw = ['podjazd', 'prosimy o korzystanie', 'można również korzystać z tramwajowej linii', 'można również korzystać z']

TOKENS = [
    Between,
    Replacement_Service,
    Not_Functioning,
    Reduced_Service,
    Bus_service,
    Loop,
    Metro_Replacement_Names,
    # Full_Stop,
    On,
    Recommended_Detour
]