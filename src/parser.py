from .tokens import TokenType
from .commands.interface import ICommand

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> ICommand:
        # TODO: Implement recursive descent parsing
        pass
