from enum import Enum, auto

class Tokens(Enum):
    VERB = auto()       # CREATE, NUKE, SHOW
    PATH =auto()
    TYPE = auto()     # Typ
    NAME = auto() # "filename.txt"
    KEYWORD = auto()    # IN, WHERE, FROM