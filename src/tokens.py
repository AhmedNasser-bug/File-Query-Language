'''
Docstring for tokens

Defines the various token types used in the lexer.
Each token type is represented as an enumeration for clarity and ease of use.

Ex:
    from enum import Enum, auto

    class Tokens(Enum):
        VERB = auto()       # CREATE, NUKE, SHOW
        PATH =auto()
        TYPE = auto()     # Typ
        NAME = auto() # "filename.txt"
        KEYWORD = auto()    # IN, WHERE, FROM
'''
from enum import Enum, auto

class Tokens(Enum):
    VERB = auto()       # CREATE, NUKE, SHOW
    PATH =auto()
    TYPE = auto()     # Typ
    NAME = auto() # "filename.txt"
    KEYWORD = auto()    # IN, WHERE, FROM