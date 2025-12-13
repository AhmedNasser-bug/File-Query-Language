import os
from . import interface
from Lexer.language import TokenTypes
from commands.utils import *

TOKEN_TYPE = 1
TOKEN_VALUE = 0

class CreateCommand(interface.ICommand):
    '''
    This class represents a command to create a file or directory.
    methods:
        - __init__(tokens:list): Initializes the command with a list of tokens.
        - command(tokens:list): Static method to create a CreateCommand instance.
        - validate() -> bool: Validates the token structure for the create command.\
        - execute() -> str: Executes the create command and returns a status message.
    properties:
        - path: The path where the file/directory will be created.
        - data: The name of the file/directory to be created.
    '''
    def __init__(self, tokens:list): 
        self.tokens=tokens
        self.validate()
    @staticmethod    
    def command(tokens:list):
        return CreateCommand(tokens)

    def validate(self) -> bool:
        if len(self.tokens)==3:
            if (self.tokens[1][TOKEN_TYPE] != TokenTypes.TYPE) or ( self.tokens[2][TOKEN_TYPE] != TokenTypes.NAME ) :
                print("not a corrert CREATE Command format,check the command order")  
                return False 
            self.path = os.curdir
            self.data = self.tokens[2][TOKEN_VALUE]
            return True
        elif len(self.tokens)==5:  
            if (self.tokens[1][TOKEN_TYPE] != TokenTypes.TYPE) or ( self.tokens[2][TOKEN_TYPE] != TokenTypes.NAME ) or ( self.tokens[3][TOKEN_TYPE] != TokenTypes.KEYWORD ) or ( self.tokens[4][TOKEN_TYPE] != TokenTypes.PATH ) :
                print("not a corrert CREATE Command format,check the command order")  
                return False 
            if self.tokens[3][TOKEN_VALUE].lower() !="in": 
                print("not a corrert CREATE Command format,wrong keyword")
                return False
            self.path = self.tokens[4][TOKEN_VALUE]
            self.data = self.tokens[2][TOKEN_VALUE]
            return True

        else:
            print("not a corrert CREATE Command format,maype you forget something")
            return False

    def execute(self) -> str:
        
        if self.validate():
            if self.tokens[1][0].lower()=="file":
                return f"CREATE {self.tokens[1][TOKEN_VALUE]} {self.data} IN {self.path}" if create_file(self.path,self.data) else f"FAILED TO CREATE {self.tokens[1][TOKEN_VALUE]} {self.data} IN {self.path}"
            if self.tokens[1][0].lower()=="folder":
                return f"CREATE {self.tokens[1][TOKEN_VALUE]} {self.data} IN {self.path}" if create_folder(self.path,self.data) else f"FAILED TO CREATE {self.tokens[1][TOKEN_VALUE]} {self.data} IN {self.path}"

        return "something went wrong"


class ReplaceCommand(interface.ICommand):
    '''
    This class represents a command to replace a file with another file.
    methods:
        - __init__(tokens:list): Initializes the command with a list of tokens.
        - command(tokens:list): Static method to create a ReplaceCommand instance.
        - validate() -> bool: Validates the token structure for the replace command.
        - execute() -> str: Executes the replace command and returns a status message.
    properties:
        - OldPath: The path of the file to be replaced.
        - NewPath: The path of the new file.  
        - tokens: The list of tokens representing the command.
    '''
    @staticmethod    
    def command(tokens:list):
        return ReplaceCommand(tokens)
    def __init__(self, tokens):
        self.tokens=tokens
        self.validate()

    def validate(self) -> bool:
        if len(self.tokens)!=4:
            print("not a correct REPLACE Command format, maybe you forget something")
            return False
        
        if ( self.tokens[1][TOKEN_TYPE] != TokenTypes.PATH) or ( self.tokens[2][TOKEN_TYPE] != TokenTypes.KEYWORD ) or ( self.tokens[3][TOKEN_TYPE] != TokenTypes.PATH ) :
           print("not a correct REPLACE Command format, check the command order")  
           return False 
        if self.tokens[2][TOKEN_VALUE].lower() !="with": 
            print(f"not a correct REPLACE Command format,wrong keyword, expected 'with' found '{self.tokens[2][TOKEN_VALUE]}'")
            return False
        self.OldPath=self.tokens[1][TOKEN_VALUE]
        self.NewPath=self.tokens[3][TOKEN_VALUE]
        
        return True

    def execute(self) -> str:
        return f"REPLACE {self.OldPath} WITH {self.NewPath}" if smart_move(self.NewPath,open(self.OldPath).read()) else f"FAILED TO REPLACE {self.OldPath} WITH {self.NewPath}"

class DeleteCommand(interface.ICommand):
    '''
    This class represents a command to delete a file or directory.
    methods:
        - __init__(tokens:list): Initializes the command with a list of tokens.++++++
        - command(tokens:list): Static method to create a DeleteCommand instance.
        - validate() -> bool: Validates the token structure for the delete command.
        - execute() -> str: Executes the delete command and returns a status message.
    properties:
        - path: The path where the file/directory to be deleted is located.
        - data: The name of the file/directory to be deleted.
    '''
    @staticmethod    
    def command(tokens:list):
        return DeleteCommand(tokens)

    def __init__(self, tokens:list): 
        self.tokens=tokens
        self.validate()

    def validate(self) -> bool:
        if len(self.tokens)==2:
            if (self.tokens[1][TOKEN_TYPE] != TokenTypes.NAME ) :
                print("not a corrert DELETE Command format,check the command order")  
                return False 
            self.path = os.getcwd()
            self.data = self.tokens[1][TOKEN_VALUE]
            return True
        elif len(self.tokens)==4:  
            if  ( self.tokens[1][TOKEN_TYPE] != TokenTypes.NAME ) or ( self.tokens[2][TOKEN_TYPE] != TokenTypes.KEYWORD ) or ( self.tokens[3][TOKEN_TYPE] != TokenTypes.PATH ) :
                print("not a corrert CREATE Command format,check the command order")  
                return False 
            if self.tokens[3][TOKEN_VALUE].lower() !="in": 
                print("not a corrert CREATE Command format,wrong keyword")
                return False
            self.path = self.tokens[3][TOKEN_VALUE]
            self.data = self.tokens[1][TOKEN_VALUE]
            return True

    def execute(self) -> str:
        return f"DELETED {self.data} IN {self.path}" if delete_dir(self.path) else f"FAILED TO DELETE {self.data} IN {self.path}"
    
class FindCommand(interface.ICommand):
    '''
    This class represents a command to find files or directories matching a pattern.
    methods:
        - __init__(tokens:list): Initializes the command with a list of tokens.
        - command(tokens:list): Static method to create a FindCommand instance.
        - validate() -> bool: Validates the token structure for the find command.
        - execute() -> str: Executes the find command and returns a status message.
    properties:
        - data: The pattern to search for.
        - tokens: The list of tokens representing the command.
    '''
    @staticmethod
    def command(tokens:list):
        return FindCommand(tokens)
    def __init__(self, tokens:list): 
        self.tokens=tokens
        self.validate()
        
    def validate(self) -> bool:
        if len(self.tokens)!=4 and len(self.tokens)!=2:
            print("not a correct FIND Command format, maybe you forget something")
            return False
        if len(self.tokens)==4:
            if ( self.tokens[1][TOKEN_TYPE] != TokenTypes.NAME ) or ( self.tokens[2][TOKEN_TYPE].lower() != 'in') or ( self.tokens[3][TOKEN_TYPE] != TokenTypes.PATH ) :
             print("not a correct FIND Command format, check the command order")  
             return False   
            self.path = self.tokens[3][TOKEN_VALUE]
            self.data = self.tokens[1][TOKEN_VALUE]
            return True
        elif len(self.tokens)==2:
            self.path = os.getcwd()
            self.data = self.tokens[1][TOKEN_VALUE]
            return True
        else:
            return False

        
    def execute(self) -> str:
        res = find_by_name(self.path,self.data)
        return f"FOUND {len(res['files']) + len(res['folders'])} items matching {self.data}"
    
class GoCommand(interface.ICommand):
    '''
    This class represents a command to change the current working directory.
    methods:
        - __init__(tokens:list): Initializes the command with a list of tokens.
        - command(tokens:list): Static method to create a GoCommand instance.
        - validate() -> bool: Validates the token structure for the go command.
        - execute() -> str: Executes the go command and returns a status message.
    properties:
        - path: The path to change the current working directory to.
        - tokens: The list of tokens representing the command.
    '''
    @staticmethod    
    def command(tokens:list):
        return GoCommand(tokens)
    
    def __init__(self, tokens:list): 
        self.tokens=tokens
        self.validate()

    def validate(self) -> bool:
            if len(self.tokens)!=2:
                print("not a correct GO Command format, maybe you forget something")
                return False
            if (self.tokens[1][TOKEN_TYPE] == TokenTypes.NAME) or (self.tokens[1][TOKEN_TYPE] == TokenTypes.PATH) :
                self.path=self.tokens[1][TOKEN_VALUE]
                return True
            else:
                print("not a correct GO Command format, check the command order")  
                return False
    def execute(self):
        return go(self.path)


class HelpCommand(interface.ICommand):
    '''
    This class represents a command to display the help menu.
    '''
    @staticmethod
    def command(tokens: list):
        return HelpCommand(tokens)

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.validate()

    def validate(self) -> bool:
        if len(self.tokens) != 1:
            print("HELP command does not take arguments")
            return False
        return True

    def execute(self) -> str:
        return """
Available Commands:
-------------------
1. CREATE:
   - create file "filename" in "path"
   - create folder "foldername" in "path"

2. REPLACE:
   - replace "old_file_path" with "new_file_path"

3. DELETE:
   - delete "filename" in "path" (if path provided)
   - delete "filename" (uses current directory)

4. FIND:
   - find "pattern" "path"

5. GO:
   - go "path" (Change directory)
   
6. CURDIR:
   - curdir (Show current directory)

7. HELP:
   - help (Show this menu)
"""


class CurdirCommand(interface.ICommand):
    '''
    This class represents a command to display the current working directory.
    '''
    @staticmethod
    def command(tokens: list):
        return CurdirCommand(tokens)

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.validate()

    def validate(self) -> bool:
        if len(self.tokens) != 1:
            print("CURDIR command does not take arguments")
            return False
        return True

    def execute(self) -> str:
        return f"Current Directory: {os.getcwd()}"
