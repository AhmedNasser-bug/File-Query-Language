import sys
from lexer import Lexer
from parser import Parser

import ctypes
import os


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


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
    # 1. Check for Admin Rights
    if not is_admin():
        print("Requesting administrator privileges...")
        
        # 2. Re-run the program with 'runas' (Admin) verb
        # sys.executable = path to python.exe
        # sys.argv = arguments passed to the script
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
        except Exception as e:
            print(f"Failed to elevate: {e}")
            
        # 3. Exit the non-admin instance
        sys.exit()

    # 4. Run the REPL (Now running as Admin)
    repl()
