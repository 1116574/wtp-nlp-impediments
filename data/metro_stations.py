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
        return ([self.name] + self.forms).__iter__()

    def __hash__(self) -> int:
        return (self.name + ''.join(self.forms)).__hash__()


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
    Station('A17', 'Dworzec Gdański', ['Dw.Gdański', 'Dw. Gdański', 'Gdański'], True),
    Station('A18', 'Plac Wilsona', ['Pl.Wilsona', 'Pl. Wilsona', 'pl.Wilsona', 'plac Wilsona'], True),
    Station('A19', 'Marymont', []),
    Station('A20', 'Słodowiec', [], True),
    Station('A21', 'Stare Bielany', []),
    Station('A22', 'Wawrzyszew', []),
    Station('A23', 'Młociny', [], True),
]

M2 = [
    Station('C6', 'Księcia Janusza', ['Ks. Janusza'], True),
    Station('C7', 'Młynów', []),
    Station('C8', 'Płocka', []),
    Station('C9', 'Rondo Daszyńskiego', [], True),
    Station('C10', 'Rondo ONZ', [], True),
    Station('C11', 'Świętokrzyska', []),
    Station('C12', 'Nowy Świat-Uniwersytet', []),
    Station('C13', 'Centrum Nauki Kopernik', []),
    Station('C14', 'Stadion Narodowy', ['Narodowy', 'Stadion']),
    Station('C15', 'Dworzec Wileński', ['Dw. Wileński', 'Wileński', 'Dw.Wileński'], True),
    Station('C16', 'Szwedzka', []),
    Station('C17', 'Targówek Mieszkaniowy', ['Targówek'], True),
    Station('C18', 'Trocka', [], True),
]
