from dataclasses import dataclass


@dataclass
class Reason_is:
    raw = ['Z powodu','Z przyczyn', 'Z przyczyny']

class Orphaned_Luggage:
    api_name = 'luggage'
    raw = ['pozostawionego bagażu', 'zostawionego bagażu', 'pozostawienia bagażu', 'zostawienia bagażu']

class Technical:
    api_name = 'technical'
    raw = ['technicznych', 'awari']

class Terrorist_Attack:
    api_name = 'terrorism'
    raw = ['ataku terrorystycznego', 'pozostawionej bomby']

class Incident:
    api_name = 'incident'
    raw = ['zdarzenia', 'wypadku']



REASONS = [
    Reason_is,
    Orphaned_Luggage,
    Technical,
    Terrorist_Attack,
    Incident,
]
