from ctypes import Union
from dataclasses import dataclass

@dataclass
class Token:
    """ Generic word token """
    pass
    # raw: list
    # name: str

    # def __repr__(self):
    #     return f'< {self.name} >'

@dataclass
class Between(Token):
    """ Joins 2 or more stations """
    raw = ['↔', '–', '<>', '<->']
    name = '+'

@dataclass
class Replacement_Service(Token):
    raw = ['zastępcza linia', 'linia zastępcza', 'zastępcza', 'linię zastępczą', 'zastępczą', 'zastepczą', 'zastępczej', 'uruchomiono']
    name = 'replacement'


@dataclass
class Not_Functioning(Token):
    raw = ['nie funkcjonują', 'nie kursują', 'wstrzymany', 'wstrzymane']
    name = 'not_functioning'

@dataclass
class Not_Functioning_Facility(Token):
    raw = ['wejście', 'wyjście', 'wind']
    name = 'not_functioning'

@dataclass
class Not_Functioning_Station(Token):
    raw = ['Wyłączone stacje z ruchu', 'wyłączone', 'Zamknięte zostały stacje metra', 'zamknięt']
    name = 'not_functioning'

@dataclass
class Reduced_Service(Token):
    raw = ['zmniejszoną częstotliwością']
    name = 'reduced'

@dataclass
class Shortened_Service(Token):
    raw = ['kursuje na trasie skróconej', 'kursują na trasie skróconej', 'na trasie skróconej']
    name = 'reduced'

@dataclass
class Tram_service(Token):
    raw = ['tramwajowa', 'tramwajowej', 'tramwaj']

@dataclass
class Bus_service(Token):
    raw = ['autobusowa', 'autobusowej', 'autobus']
    name = 'bus'

@dataclass
class Loop(Token):
    raw = ['pętli']

@dataclass
class Loop_Double(Token):
    raw = ['dwóch pętlach', 'pętlach']

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
class On_Station(Token):
    raw = ['na stacji']

@dataclass
class Recommended_Detour(Token):
    raw = ['prosimy o korzystanie', 'prosimy również o korzystanie', 'można również korzystać z tramwajowej linii', 'można również korzystać z']

@dataclass
class Detour_By_Extension(Token):
    raw = ['podjazd', 'na trasę wydłużoną', 'trasie wydłużonej', 'wydłużone',]

class Metro_Line:
    __match_args__ = ('line',)

    def __init__(self, line) -> None:
        self.line = line

    def __repr__(self) -> str:
        return f'< {self.line} >'
    
    @property
    def raw(self):
        return [f'linia metra {self.line}', f'linii metra {self.line}', f'metra linii {self.line}', self.line]


class Reason:
    __match_args__ = ('reason',)

    def __init__(self, reason) -> None:
        self.reason = reason

    def __repr__(self) -> str:
        return f'< Reason: {self.reason} >'
    
    @property
    def raw(self):
        return [f'Z powodu {self.reason}',f'Z przyczyn {self.reason}']

TOKENS = [
    Between,
    Replacement_Service,
    Not_Functioning,
    Not_Functioning_Facility,
    Not_Functioning_Station,
    Reduced_Service,
    Shortened_Service,
    Detour_By_Extension,
    Bus_service,
    Tram_service,
    Loop,
    Loop_Double,
    Metro_Replacement_Names,
    # Full_Stop,
    On,
    Recommended_Detour,
    Metro_Line('M1'),
    Metro_Line('M2'),
    Reason('awari'),
    Reason('zdarzenia'),
    Reason('pozostawionego bagażu'),
    Reason('technicznych'),
    On_Station
]