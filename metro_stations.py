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
from turtle import st

@dataclass
class Station:
    """ Metro station """
    id: str
    name: str
    forms: list
    turn_around: bool = False

    def __repr__(self):
        return f'< {self.name} >'

    def __iter__(self):
        return ([self.name] + self.forms).__iter__()


M1 = [
    Station('A1', 'Kabaty', [], True),
    Station('A2', 'Natolin', []),
    Station('A3', 'Imielin', []),
    Station('A4', 'Stokłosy', [], True),
    Station('A5', 'Ursynów', []),
    Station('A6', 'Służew', ['Służewiec']),
    Station('A7', 'Wilanowska', [], True),
    Station('A8', 'Wierzbno', []),
    Station('A9', 'Racławicka', []),
    Station('A10', 'Pole Mokotowskie', []),
    Station('A11', 'Politechnika', [], True),
    Station('A13', 'Centrum', [], True),
    Station('A14', 'Świętokrzyska', []),
    Station('A15', 'Ratusz Arsenał', ['Ratusz-Arsenał']),
    Station('A17', 'Dworzec Gdański', ['Dw.Gdański', 'Dw. Gdański'], True),
    Station('A18', 'Plac Wilsona', ['Pl.Wilsona', 'Pl. Wilsona', 'pl.Wilsona', 'plac Wilsona'], True),
    Station('A19', 'Marymont', []),
    Station('A20', 'Słodowiec', [], True),
    Station('A21', 'Stare Bielany', []),
    Station('A22', 'Wawrzyszew', []),
    Station('A23', 'Młociny', [], True),
]
