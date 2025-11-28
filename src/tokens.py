from enum import Enum, auto

class TokenType(Enum):
    VERB = auto()       # TOUCH, NUKE, SHOW
    TARGET = auto()     # FILE, FILES, LINES
    STRING = auto()     # "filename.txt"
    KEYWORD = auto()    # IN, WHERE, FROM
    EOF = auto()
