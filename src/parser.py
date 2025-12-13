'''
Docstring for src.parser

This module contains the Parser class which is responsible for parsing
a list of tokens and returning the corresponding command object.
'''


from commands.interface import ICommand
from commands.file_ops import *

commands={
    "create":CreateCommand.command,
    "replace": ReplaceCommand.command,
    "delete":DeleteCommand.command,
    "find":FindCommand.command,
    "go":GoCommand.command,
    "help":HelpCommand.command,
    "curdir":CurdirCommand.command
}

class Parser:
    def __init__(self, tokens:list):
        self.tokens = tokens
    def parse(self) -> ICommand:
        op = commands[self.tokens[0][TOKEN_VALUE]](self.tokens)
        return op
