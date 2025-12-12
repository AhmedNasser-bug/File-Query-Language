import os
from . import interface
from tokens import Tokens
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
    @staticmethod    
    def command(tokens:list):
        return CreateCommand(tokens)

    def validate(self) -> bool:
        if len(self.tokens)==3:
            if (self.tokens[1][TOKEN_TYPE] != Tokens.TYPE) or ( self.tokens[2][TOKEN_TYPE] != Tokens.NAME ) :
                print("not a corrert CREATE Command format,check the command order")  
                return False 
            self.path = os.curdir
            self.data = self.tokens[2][TOKEN_VALUE]
            return True
        elif len(self.tokens)==5:  
            if (self.tokens[1][TOKEN_TYPE] != Tokens.TYPE) or ( self.tokens[2][TOKEN_TYPE] != Tokens.NAME ) or ( self.tokens[3][TOKEN_TYPE] != Tokens.KEYWORD ) or ( self.tokens[4][TOKEN_TYPE] != Tokens.PATH ) :
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

    def validate(self) -> bool:
        if len(self.tokens)!=4:
            print("not a correct REPLACE Command format, maybe you forget something")
            return False
        
        if ( self.tokens[1][TOKEN_TYPE] != Tokens.PATH) or ( self.tokens[2][TOKEN_TYPE] != Tokens.KEYWORD ) or ( self.tokens[3][TOKEN_TYPE] != Tokens.PATH ) :
           print("not a correct REPLACE Command format, check the command order")  
           return False 
        if self.tokens[2][TOKEN_VALUE].lower() !="with": 
            print(f"not a correct REPLACE Command format,wrong keyword, expected 'with' found '{self.tokens[2][TOKEN_VALUE]}'")
            return False
        self.OldPath=self.tokens[1][TOKEN_VALUE]
        self.NewPath=self.tokens[3][TOKEN_VALUE]
        
        return True

    def execute(self) -> str:
        if self.validate():
            return f"REPLACE {self.OldPath} WITH {self.NewPath}" if smart_move(self.NewPath,open(self.OldPath).read()) else f"FAILED TO REPLACE {self.OldPath} WITH {self.NewPath}"
        return "something went wrong"

class DeleteCommand(interface.ICommand):
    '''
    This class represents a command to delete a file or directory.
    methods:
        - __init__(tokens:list): Initializes the command with a list of tokens.
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

    def validate(self) -> bool:
        if len(self.tokens)==2:
            if (self.tokens[1][TOKEN_TYPE] != Tokens.NAME ) :
                print("not a corrert DELETE Command format,check the command order")  
                return False 
            self.path = os.curdir
            self.data = self.tokens[1][TOKEN_VALUE]
            return True
        elif len(self.tokens)==4:  
            if  ( self.tokens[1][TOKEN_TYPE] != Tokens.NAME ) or ( self.tokens[2][TOKEN_TYPE] != Tokens.KEYWORD ) or ( self.tokens[3][TOKEN_TYPE] != Tokens.PATH ) :
                print("not a corrert CREATE Command format,check the command order")  
                return False 
            if self.tokens[3][TOKEN_VALUE].lower() !="in": 
                print("not a corrert CREATE Command format,wrong keyword")
                return False
            self.path = self.tokens[3][TOKEN_VALUE]
            self.data = self.tokens[1][TOKEN_VALUE]
            return True


    def execute(self) -> str:
        # todo im
        if self.validate():
            return f"DELETE {self.data} IN {self.path}" if delete_dir(self.path) else f"FAILED TO DELETE {self.data} IN {self.path}"
        return "something went wrong"
    
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
        
    def validate(self) -> bool:
        if len(self.tokens)!=4:
            print("not a correct FIND Command format, maybe you forget something")
            return False
        
        if ( self.tokens[1][TOKEN_TYPE] != Tokens.NAME ) or ( self.tokens[2][TOKEN_TYPE] != Tokens.PATH ):
           print("not a correct FIND Command format, check the command order")  
           return False   
    
        self.data = self.tokens[1][TOKEN_VALUE]
        
        return True
    def execute(self) -> str:
        if self.validate():
            res = scan_directory(".",""+self.data+"")
            return f"FOUND {res} items matching {self.data}"
        return "something went wrong"
    
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
    def validate(self) -> bool:
            if len(self.tokens)!=2:
                print("not a correct GO Command format, maybe you forget something")
                return False
            if (self.tokens[1][TOKEN_TYPE] == Tokens.NAME) or (self.tokens[1][TOKEN_TYPE] == Tokens.PATH) :
                self.path=self.tokens[1][TOKEN_VALUE]
                return True
            else:
                print("not a correct GO Command format, check the command order")  
                return False
    def execute(self):
        if self.validate():
            return go(self.path)
        return "something went wrong"