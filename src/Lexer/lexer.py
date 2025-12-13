from Lexer.language import Language, TokenTypes


class Lexer:
    def __init__(self, source_code: str):
        self.source = source_code
        self.words = self.get_raw_words()

    def get_raw_words(self):
        raw_words = []

        for word in self.source.split():
            if Language.is_string(word): # have qoutes (name, path)
                raw_words.append(f'{word[1:-1]}')  # Strip quotes "ahmed" -> ahmed
                continue
            else: # anything else
                word = word.lower().strip()
                raw_words.append(word)
            
        return raw_words

    def get_token_type(self, word: str):
        if word in Language.word_types:
            return Language.word_types[word]
        else:
            if Language.validate_filename(word):
                return TokenTypes.NAME
            elif Lexer.validate_path(word):
                return TokenTypes.PATH


        raise ValueError(f"Unknown token: {word}")
    
    def tokenize(self):
        tokens_result = []
        
        for word in self.words:
            tokens_result.append((word, self.get_token_type(word))) 

        return tokens_result
    
if __name__ == "__main__":
    code = 'go "d:/"'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print(tokens)