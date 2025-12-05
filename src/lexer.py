from tokens import Tokens
import validation

lang = {
    "CREATE": Tokens.VERB,
    "REPLACE": Tokens.VERB,
    "FIND" :Tokens.VERB,
    "DELETE":Tokens.VERB,
    "FILE": Tokens.TYPE,
    "DIR": Tokens.TYPE,
    "With":Tokens.KEYWORD,
    "IN": Tokens.KEYWORD,
    "WHERE": Tokens.KEYWORD
}

raw = "CREATE FILE 'Ac'"
class Lexer:
    def __init__(self, source_code: str):
        self.source = source_code

    def tokenize(self):
        tokens_result = []
        words = self.source.split()
        file_type = "FILE"  # Default type
        for word in words:
            if lang[word.upper()] == Tokens.VERB:
                tokens_result.append(word ,Tokens.VERB)
            elif lang[word.upper()] == Tokens.KEYWORD:
                tokens_result.append(word.upper(), Tokens.KEYWORD)
            elif lang[word.upper()] == Tokens.TYPE:
                file_type = word.upper()
                tokens_result.append(file_type, Tokens.TYPE)
            else:
                if validation.Vlaid.is_path(word):
                    tokens_result.append(word, Tokens.PATH)
                else:
                    tokens_result.append(word, Tokens.NAME)
        return tokens_result