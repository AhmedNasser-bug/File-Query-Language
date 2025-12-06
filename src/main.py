import sys
from lexer import Lexer
from parser import Parser

def repl():
    print("FQL v0.1 - File Query Language")
    print("Type 'exit' to quit.")
    while True:
        try:
            text = input("FQL > ")
            if text == "exit": break
            lexer = Lexer(text)
            parser = Parser(lexer.tokenize())
            result = parser.parse().execute()
            print(result)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
