from dataclasses import dataclass

@dataclass
class _Reason:
    length: int = 0
    index: int = 0
    word_index: int = 0
    text: str = ''

@dataclass
class Reason_is(_Reason):
    raw = ['Z powodu','Z przyczyn', 'Z przyczyny', 'w wyniku', 'w związku']

class Orphaned_Luggage(_Reason):
    api_name = 'luggage'
    raw = ['pozostawionego bagażu', 'pozostawionym bagażem', 'zostawionego bagażu', 'pozostawienia bagażu', 'zostawienia bagażu', 'zostawionym bagażem']

class Technical(_Reason):
    api_name = 'technical'
    raw = ['technicznych', 'awari']

class Terrorist_Attack(_Reason):
    api_name = 'terrorism'
    raw = ['ataku terrorystycznego', 'pozostawionej bomby']

class Incident(_Reason):
    api_name = 'incident'
    raw = ['zdarzenia', 'zdarzeniem', 'wypadku']



REASONS = [
    Reason_is,
    Orphaned_Luggage,
    Technical,
    Terrorist_Attack,
    Incident,
]
