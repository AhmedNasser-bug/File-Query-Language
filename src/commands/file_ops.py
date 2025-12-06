from . import interface
from tokens import Tokens
from commands.utils import *

TOKEN_TYPE = 1
TOKEN_VALUE = 0

class CreateCommand(interface.ICommand):
    def __init__(self, tokens:list): 
        self.tokens=tokens
    @staticmethod    
    def command(tokens:list):
        return CreateCommand(tokens)

    def validate(self) -> bool:
        if len(self.tokens)!=5:
            print("not a corrert CREATE Command format,maype you forget something")
            return False
        
        if (self.tokens[1][TOKEN_TYPE] != Tokens.TYPE) or ( self.tokens[2][TOKEN_TYPE] != Tokens.NAME ) or ( self.tokens[3][TOKEN_TYPE] != Tokens.KEYWORD ) or ( self.tokens[4][TOKEN_TYPE] != Tokens.PATH )  :
           print("not a corrert CREATE Command format,check the command order")  
           return False   
        if self.tokens[3][TOKEN_VALUE].lower() !="in": 
            print("not a corrert CREATE Command format,wrong keyword")
            return False
        self.path = self.tokens[4][TOKEN_VALUE]
        self.data = self.tokens[2][TOKEN_VALUE]
        
        return True

    def execute(self) -> str:
        
        if self.validate():
            
            return f"CREATE {self.tokens[1][TOKEN_VALUE]} {self.data} IN {self.path}" if create_file(self.path,self.data) else f"FAILED TO CREATE {self.tokens[1][TOKEN_VALUE]} {self.data} IN {self.path}"
        return "something went wrong"


class RepalceCommand(interface.ICommand):

    @staticmethod    
    def command(tokens:list):
        return RepalceCommand(tokens)
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
    @staticmethod    
    def command(tokens:list):
        return DeleteCommand(tokens)

    def __init__(self, tokens:list): 
        self.tokens=tokens

    def validate(self) -> bool:
        if len(self.tokens)!=4:
            print("not a correct DELETE Command format, maybe you forget something")
            return False
        
        if ( self.tokens[1][TOKEN_TYPE] != Tokens.NAME ) or ( self.tokens[2][TOKEN_TYPE] != Tokens.KEYWORD ) or ( self.tokens[3][TOKEN_TYPE] != Tokens.PATH )  :
           print("not a correct DELETE Command format, check the command order")  
           return False   
        if self.tokens[2][TOKEN_VALUE].lower() !="in": 
            print(f"not a correct DELETE Command format, wrong keyword, expected 'in' found '{self.tokens[2][TOKEN_VALUE]}'")
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

    @staticmethod
    def command(tokens:list):
        return FindCommand(tokens)
    def __init__(self, tokens:list): 
        self.tokens=tokens
        
    def validate(self) -> bool:
        if len(self.tokens)!=2:
            print("not a correct FIND Command format, maybe you forget something")
            return False
        
        if ( self.tokens[1][TOKEN_TYPE] != Tokens.NAME ) or ( self.tokens[2][TOKEN_TYPE] != Tokens.PATH ):
           print("not a correct FIND Command format, check the command order")  
           return False   
    
        self.data = self.tokens[1][TOKEN_VALUE]
        
        return True
    def execute(self) -> str:
        if self.validate():
            res = scan_directory(".","*"+self.data+"*")
            return f"FOUND {res} items matching {self.data}"
        return "something went wrong"