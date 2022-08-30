"""

'A23' 'Młociny'
'A20' 'Słodowiec'
'A18' 'Plac Wilsona', 'Pl.Wilsona'
'A17' 'Dworzec Gdański', 'Dw.Gdański'
'A13' 'Centrum'
'A11' 'Politechnika'
'A7' 'Wilanowska'
'A4' 'Stokłosy'
'A1' 'Kabaty'

'C6' 'Księcia Janusza'
'C9' 'Rondo Daszyńskiego'
'C10' 'Rondo ONZ'
'C15' 'Dworzec Wileński', 'Dw.Wileński'
'C17' 'Targówek mieszkaniowy'
'C18' 'Trocka'

"""

from dataclasses import dataclass

@dataclass
class Station:
    """ Metro station """
    id: str
    name: str
    forms: list
    turn_around: bool = False

    __match_args__ = ('id', 'name', 'forms', 'turn_around')

    def __repr__(self):
        return f'< {self.name} >'

    def __iter__(self):
        return (['Metro ' + self.name, self.name] + self.forms).__iter__()

    def __hash__(self) -> int:
        return (self.name + ''.join(self.forms)).__hash__()

    def __str__(self) -> str:
        return self.id


A1 = Station('A1', 'Kabaty', ['Kabat'], True)
A2 = Station('A2', 'Natolin', ['Natolina'])
A3 = Station('A3', 'Imielin', ['Imielina'])
A4 = Station('A4', 'Stokłosy', [], True)
A5 = Station('A5', 'Ursynów', [])
A6 = Station('A6', 'Służew', ['Służewiec'])
A7 = Station('A7', 'Wilanowska', ['Wilanowskiej'], True)
A8 = Station('A8', 'Wierzbno', ['Wierzbna'])
A9 = Station('A9', 'Racławicka', [])
A10 = Station('A10', 'Pole Mokotowskie', ['Pola Mokotowskiego'])
A11 = Station('A11', 'Politechnika', [], True)
A13 = Station('A13', 'Centrum', [], True)
A14 = Station('A14', 'Świętokrzyska', ['Świętokrzyskiej'])
A15 = Station('A15', 'Ratusz Arsenał', ['Ratusz-Arsenał', 'Ratuszu Arsenał'])
A17 = Station('A17', 'Dworzec Gdański', ['Dw.Gdański', 'Dw. Gdański', 'Gdański'], True)
A18 = Station('A18', 'Plac Wilsona', ['Pl.Wilsona', 'Pl. Wilsona', 'pl.Wilsona', 'plac Wilsona'], True)
A19 = Station('A19', 'Marymont', ['Marymontu'])
A20 = Station('A20', 'Słodowiec', ['Słodowca'], True)
A21 = Station('A21', 'Stare Bielany', ['Starych Bielan'])
A22 = Station('A22', 'Wawrzyszew', [])
A23 = Station('A23', 'Młociny', ['Młocin'], True)

C4 = Station('C4', 'Bemowo', [], True)
C5 = Station('C5', 'Ulrychów', [], False)
C6 = Station('C6', 'Księcia Janusza', ['Ks. Janusza', 'Ks.Janusza'], True)
C7 = Station('C7', 'Młynów', [])
C8 = Station('C8', 'Płocka', [])
C9 = Station('C9', 'Rondo Daszyńskiego', [], True)
C10 = Station('C10', 'Rondo ONZ', [], True)
C11 = Station('C11', 'Świętokrzyska', [])
C12 = Station('C12', 'Nowy Świat-Uniwersytet', [])
C13 = Station('C13', 'Centrum Nauki Kopernik', [])
C14 = Station('C14', 'Stadion Narodowy', ['Narodowy', 'Stadion'])
C15 = Station('C15', 'Dworzec Wileński', ['Dw. Wileński', 'Wileński', 'Dw.Wileński'], True)
C16 = Station('C16', 'Szwedzka', [])
C17 = Station('C17', 'Targówek Mieszkaniowy', ['Targówek'], True)
C18 = Station('C18', 'Trocka', [], True)

M1 = [
    A1,
    A2,
    A3,
    A4,
    A5,
    A6,
    A7,
    A8,
    A9,
    A10,
    A11,
    A13,
    A14,
    A15,
    A17,
    A18,
    A19,
    A20,
    A21,
    A22,
    A23,
]

M2 = [
    C4,
    C5,
    C6,
    C7,
    C8,
    C9,
    C10,
    C11,
    C12,
    C13,
    C14,
    C15,
    C16,
    C17,
    C18,
]
