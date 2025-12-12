from tokens import Tokens
from validation import *

lang = {
    "create": Tokens.VERB,
    "replace": Tokens.VERB,
    "find" :Tokens.VERB,
    "delete":Tokens.VERB,
    "file": Tokens.TYPE,
    "dir": Tokens.TYPE,
    "with":Tokens.KEYWORD,
    "in": Tokens.KEYWORD,
    "where": Tokens.KEYWORD
}



class Lexer:
    def __init__(self, source_code: str):
        self.source = source_code
        self.words = self.get_raw_words()

    def get_raw_words(self):
        raw_words = []

        for word in self.source.split():
            if is_string(word): # have qoutes (name, path)
                raw_words.append(f'{word[1:-1]}')  # Strip quotes "ahmed" -> ahmed
                continue
            else: # anything else
                word = word.lower().strip()
                raw_words.append(word)
            
        return raw_words

    def get_token_type(self, word: str):
        if word in lang:
            return lang[word]
        else:
            if validate_filename(word):
                return Tokens.NAME
            elif validate_path(word):
                return Tokens.PATH


        raise ValueError(f"Unknown token: {word}")
    
    def tokenize(self):
        tokens_result = []
        
        for word in self.words:
            tokens_result.append((word, self.get_token_type(word)))
            
                

        return tokens_result