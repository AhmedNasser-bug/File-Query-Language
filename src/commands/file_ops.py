from interface import ICommand
from tokens import Tokens
class CreateCommand(ICommand):
    def __init__(self, tokens:list): 
        self.tokens=tokens

    def validate(self) -> bool:
        if len(self.tokens)!=5:
            print("not a corrert CREATE Command format,maype you forget something")
            return False
        
        if (self.tokens[1][1] != Tokens.TYPE) or ( self.tokens[2][1] != Tokens.NAME ) or ( self.tokens[3][1] != Tokens.KEYWORD ) or ( self.tokens[4][1] != Tokens.PATH )  :
           print("not a corrert CREATE Command format,check the command order")  
           return False   
        if self.tokens[3][1].lower() !="in": 
            print("not a corrert CREATE Command format,wrong keyword")
            return False
        self.path = self.tokens[4][0]
        self.data = self.tokens[2][0]
        
        return True

    def execute(self) -> str:
        # todo im
        if self.validate():
            return f"CREATE {self.tokens[1][0]} {self.data} IN {self.path}"
        return "something went wrong"


class RepalceCommand(ICommand):
    def __init__(self, tokens):
        self.tokens=tokens

    def validate(self) -> bool:
        if len(self.tokens)!=4:
            print("not a corrert REPALCE Command format,maype you forget something")
            return False
        
        if ( self.tokens[1][1] != Tokens.PATH) or ( self.tokens[2][1] != Tokens.KEYWORD ) or ( self.tokens[3][1] != Tokens.PATH ) :
           print("not a corrert REPALCE Command format,check the command order")  
           return False 
        if self.tokens[2][1].lower() !="with": 
            print("not a corrert REPALCE Command format,wrong keyword")
            return False
        self.OldPath=self.tokens[1][0]
        self.NewPath=self.tokens[2][0]
        
        return True

    def execute(self) -> str:
        if self.validate():
            return f"REPALCE {self.OldPath} WITH {self.NewPath}"
        return "something went wrong"

class DeleteCommand(ICommand):
    def __init__(self, tokens:list): 
        self.tokens=tokens

    def validate(self) -> bool:
        if len(self.tokens)!=4:
            print("not a corrert DELETE Command format,maype you forget something")
            return False
        
        if ( self.tokens[1][1] != Tokens.NAME ) or ( self.tokens[2][1] != Tokens.KEYWORD ) or ( self.tokens[3][1] != Tokens.PATH )  :
           print("not a corrert DELETE Command format,check the command order")  
           return False   
        if self.tokens[2][1].lower() !="in": 
            print("not a corrert DELETE Command format,wrong keyword")
            return False
        self.path = self.tokens[3][0]
        self.data = self.tokens[1][0]
            
        return True

    def execute(self) -> str:
        # todo im
        if self.validate():
            return f"DELETE {self.data} IN {self.path}"
        return "something went wrong"
    
class FindCommand(ICommand):
    def __init__(self, tokens:list): 
        self.tokens=tokens
        
    def validate(self) -> bool:
        if len(self.tokens)!=2:
            print("not a corrert FIND Command format,maype you forget something")
            return False
        
        if ( self.tokens[1][1] != Tokens.NAME ) or  ( self.tokens[1][1] != Tokens.PATH ):
           print("not a corrert FIND Command format,check the command order")  
           return False   
    
        self.data = self.tokens[1][0]
        
        return True
    def execute(self) -> str:
        # todo im
        if self.validate():
            return f"FIND {self.data}"
        return "something went wrong"