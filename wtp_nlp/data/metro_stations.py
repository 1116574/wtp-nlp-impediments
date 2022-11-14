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
import unicodedata
from dataclasses import dataclass

@dataclass
class Station:
    """ Metro station """
    id: str
    name: str
    forms: list
    gtfs_id: str
    length: int = 0  # to be filled at runtime
    turn_around: bool = False

    __match_args__ = ('id', 'name', 'forms', 'turn_around')

    @classmethod
    def _ascii(cls, unicode_rich_text: str) -> str:
        text = unicodedata.normalize('NFD', unicode_rich_text)
        new_text = ''
        for char in text:
            if ord(char) < 127:  # 127 is highest ascii character
                new_text += char
        
        return new_text


    def __repr__(self):
        return f'{self.id}_{self.name}(length={self.length})'

    def __iter__(self):
        all_forms = ['Metro ' + self.name, self.name] + self.forms
        for form in all_forms[:]:  # The list[:] is to create a copy of an object, since the original will be appended to in the same loop
            all_forms.append(self._ascii(form))
        
        return all_forms.__iter__()

    def __hash__(self) -> int:
        return (self.name + ''.join(self.forms)).__hash__()

    def __str__(self) -> str:
        return f'{self.id}/{self.name}'


A1 = Station('A1', 'Kabaty', ['Kabat'], '3282m', True)
A2 = Station('A2', 'Natolin', ['Natolina'], '3281m')
A3 = Station('A3', 'Imielin', ['Imielina'], '3280m')
A4 = Station('A4', 'Stokłosy', [], '3132m', True)
A5 = Station('A5', 'Ursynów', [], '3127m')
A6 = Station('A6', 'Służew', ['Służewiec'], '3279m')
A7 = Station('A7', 'Wilanowska', ['Wilanowskiej'], '3009m', True)
A8 = Station('A8', 'Wierzbno', ['Wierzbna'], '3114m')
A9 = Station('A9', 'Racławicka', [], '3230m')
A10 = Station('A10', 'Pole Mokotowskie', ['Pola Mokotowskiego'], '3228m')
A11 = Station('A11', 'Politechnika', [], '7006m', True)
A13 = Station('A13', 'Centrum', [], '7013m', True)
A14 = Station('A14', 'Świętokrzyska', ['Świętokrzyskiej'], '7014m')
A15 = Station('A15', 'Ratusz Arsenał', ['Ratusz-Arsenał', 'Ratuszu Arsenał'], '7099m')
A17 = Station('A17', 'Dworzec Gdański', ['Dw.Gdański', 'Dw. Gdański', 'Gdański', 'dworzec gdański'], '7019m', True)
A18 = Station('A18', 'Plac Wilsona', ['Pl.Wilsona', 'Pl. Wilsona', 'pl.Wilsona', 'plac Wilsona', 'plac wilsona'], '6003m', True)
A19 = Station('A19', 'Marymont', ['Marymontu'], '6005m')
A20 = Station('A20', 'Słodowiec', ['Słodowca'], '6006m', True)
A21 = Station('A21', 'Stare Bielany', ['Starych Bielan'], '6052m')
A22 = Station('A22', 'Wawrzyszew', [], '6055m')
A23 = Station('A23', 'Młociny', ['Młocin'], '6059m', True)

C4 = Station('C4', 'Bemowo', ['Bemowie'], '5034m', True)
C5 = Station('C5', 'Ulrychów', ['Ulrychowie'], '5032m', False)
C6 = Station('C6', 'Księcia Janusza', ['Ks. Janusza', 'Ks.Janusza'], '5030m', True)
C7 = Station('C7', 'Młynów', ['Młynowie'], '5028m')
C8 = Station('C8', 'Płocka', ['Płockiej'], '5005m')
C9 = Station('C9', 'Rondo Daszyńskiego', ['Ronda Daszyńskiego'], '5040m', True)
C10 = Station('C10', 'Rondo ONZ', ['Ronda ONZ'], '7088m', True)
C11 = Station('C11', 'Świętokrzyska', ['Świętokrzyskiej'], '7014m')
C12 = Station('C12', 'Nowy Świat-Uniwersytet', [], '7043m')
C13 = Station('C13', 'Centrum Nauki Kopernik', ['CNK'], '7079m')
C14 = Station('C14', 'Stadion Narodowy', ['Narodowy', 'Stadion'], '1231m')
C15 = Station('C15', 'Dworzec Wileński', ['Dw. Wileński', 'Wileński', 'Dw.Wileński'], '1003m', True)
C16 = Station('C16', 'Szwedzka', ['Szwedzkiej'], '1526m')
C17 = Station('C17', 'Targówek Mieszkaniowy', ['Targówek', 'Targówka'], '1137m', True)
C18 = Station('C18', 'Trocka', ['Trockiej'], '1140m', True)
C19 = Station('C19', 'Zacisze', ['Zacisza', 'Zaciszu'], '1411m', False)  # TODO: Add correct info about ability to turnaround on those stations
C20 = Station('C20', 'Kondratowicza', [], '1146m', False)
C21 = Station('C21', 'Bródno', ['Bródnie'], '1085m', False)

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
    C19,
    C20,
    C21,
]
