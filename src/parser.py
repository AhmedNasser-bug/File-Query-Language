'''
Docstring for src.parser

This module contains the Parser class which is responsible for parsing
a list of tokens and returning the corresponding command object.
'''




from .tokens import Tokens
from .commands.interface import ICommand
from commands.file_ops import *

commands = {
    "CREATE": CreateCommand,
}
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self) -> ICommand:
        pass
