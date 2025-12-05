from tokens import Tokens

lang = {
    "CREATE": Tokens.VERB,
    "NUKE": Tokens.VERB,
    "SHOW": Tokens.VERB,
    "FILE": Tokens.TARGET,
    "DIR": Tokens.TARGET,
    "LINES": Tokens.TARGET,
    "IN": Tokens.KEYWORD,
    "WHERE": Tokens.KEYWORD,
}

raw = "CREATE FILE 'Ac'"
class Lexer:
    def __init__(self, source_code: str):
        self.source = source_code
        
    def tokenize(self):
        self.tokens = self.source.split(" ")
        return {token: lang[token] if token in lang else Tokens.ARG for token in self.tokens}

