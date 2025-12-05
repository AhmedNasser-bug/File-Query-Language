from enum import Enum, auto

class Tokens(Enum):
    VERB = auto()       # CREATE, NUKE, SHOW
    TARGET = auto()     # FILE, FOLDER
    ARG = auto()     # "filename.txt"
    KEYWORD = auto()    # IN, WHERE, FROM
    EOF = auto()
