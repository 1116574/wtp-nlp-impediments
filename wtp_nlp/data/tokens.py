from dataclasses import dataclass

class Dummy:
    pass

class Full_Stop:
    pass

class And:
    pass

class New_Line:
    pass

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
    raw = ['↔', '–', '<–>', '<>', '-', '<->']
    name = '+'

@dataclass
class Replacement_Service(Token):
    raw = ['zastępcza linia', 'linia zastępcza', 'zastępcza', 'linię zastępczą', 'zastępczą', 'zastepczą', 'zastępczej', 'uruchomiono']
    name = 'replacement'


@dataclass
class Whole_Metro(Token):
    raw = ['obie linie metra']


@dataclass
class Not_Functioning_Service(Token):
    raw = ['nie funkcjonują', 'nie kursują', 'wstrzymany', 'wstrzymane', 'wyłączenie', 'nie kursuje']
    name = 'not_functioning'

@dataclass
class Not_Functioning_Facility(Token):
    raw = ['zamknięte wejście', 'zamknięte wyjście', 'zamknięto wejście', 'zamknięto wyjście', 'awaria wind', 'nie działają windy', 'schody ruchome', 'windy']
    name = 'not_functioning'

@dataclass
class Not_Functioning_Station(Token):
    raw = ['Wyłączone stacje z ruchu', 'wyłączone', 'Zamknięte zostały stacje metra', 'zamknięcie stacji', 'zamknięto stację', 'zostaje zamknięta', 'zamyka się']  # 'zamknię'
    name = 'not_functioning'

@dataclass
class Reduced_Service(Token):
    raw = ['zmniejszoną częstotliwością', 'utrudnienia w kursowaniu']  # 'utrudni' - za utrudnienia przepraszmy
    name = 'reduced'

@dataclass
class Shortened_Service(Token):
    raw = ['kursuje na trasie skróconej', 'kursują na trasie skróconej', 'na trasie skróconej', 'na skróconej trasie']
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


# TODO: This requires more logic to recognize abbriviaitons
# @dataclass
# class Full_Stop(Token):
#     raw = ['.']

# class Not(Token):
#     ''' General negator '''
#     raw = [' nie ']
# Disused + doesnt do anything important

@dataclass
class On(Token):
    raw = ['na trasie', 'na odcinku']


@dataclass
class Run(Token):
    raw = ['pociągi kursują', 'kursują']


@dataclass
class On_Station(Token):
    raw = ['na stacji', 'w rejonie stacji']

@dataclass
class Recommended_Detour(Token):
    raw = ['prosimy o korzystanie', 'prosimy również o korzystanie', 'można również korzystać z tramwajowej linii', 'można również korzystać z']

@dataclass
class Detour_By_Extension(Token):
    raw = ['podjazd', 'na trasę wydłużoną', 'trasie wydłużonej', 'wydłużone', 'wydłużono', 'wykonują podjazdy']

@dataclass
class Delays(Token):
    raw = ['możliwe opóźnienia', 'opóźnie']


@dataclass
class Skipping(Token):
    raw = ['z ominięciem', 'pomijając']

class Metro_Line:
    __match_args__ = ('line',)

    def __init__(self, line) -> None:
        self.line = line

    def __repr__(self) -> str:
        return f'< {self.line} >'

    def __str__(self):
        return self.line.strip()  # this is an offle fix for ' M1' -> 'M1'
    
    @property
    def raw(self):
        return [f'linia metra {self.line}', f'linii metra {self.line}', f'metra linii {self.line}', self.line]


class Reason:
    __match_args__ = ('reason',)

    def __init__(self, reason) -> None:
        self.reason = reason

    def __repr__(self) -> str:
        return f'< Reason: {self.reason} >'

    def __str__(self) -> str:
        return self.reason
    
    @property
    def raw(self):
        return [f'Z powodu {self.reason}',f'Z przyczyn {self.reason}']


class Metro_Replacement_Names:
    def __init__(self, repl_name) -> None:
        self.repl_name = repl_name
        self.raw = [repl_name]

    def __repr__(self) -> str:
        return f'< Metro_Replacement_Name: {self.repl_name} >'
    
    # @property
    # def raw(self):
    #     return [self.repl_name,]

TOKEN_M1 = Metro_Line(' M1')  # leading space to avoid matching ZM1 (the replacement bus)
TOKEN_M2 = Metro_Line(' M2')

TOKENS = [
    On,
    Run,
    On_Station,

    Between,
    Replacement_Service,
    Not_Functioning_Service,  # as in, trains dont run
    Not_Functioning_Facility,  # elevators, exits...
    Not_Functioning_Station,  # whole station closed, but no mention if trains pass throu (tho usually they dont) or if the service is split
    Reduced_Service,
    Shortened_Service,
    Detour_By_Extension,
    Bus_service,
    Tram_service,
    Loop,
    Loop_Double,
    # Metro_Replacement_Names,
    # Full_Stop,
    # Not,
    Recommended_Detour,
    TOKEN_M1,
    TOKEN_M2,
    Reason('awari'),
    Reason('zdarzenia'),
    Reason('pozostawionego bagażu'),
    Reason('zostawionego bagażu'),
    Reason('pozostawienia bagażu'),
    Reason('zostawienia bagażu'),
    Reason('pozostawionej bomby'),
    Reason('ataku terrorystycznego'),
    Reason('technicznych'),
    Delays,
    Metro_Replacement_Names('"ZA METRO"'),
    Metro_Replacement_Names('ZA METRO'),
    Metro_Replacement_Names('za "metro"'),
    Metro_Replacement_Names('za „Metro”'),  # unicode, breaking text parsing since 2002
    Metro_Replacement_Names('ZM1'),
    Metro_Replacement_Names('ZM2'),
    Metro_Replacement_Names('Z-1'),
    Metro_Replacement_Names('Z-2'),
    Metro_Replacement_Names('linii Z'),
    Skipping,
    Whole_Metro,

]
