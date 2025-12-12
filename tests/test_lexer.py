import unittest
import sys
import os

# Add 'src' to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lexer import Lexer
from tokens import Tokens

class TestLexer(unittest.TestCase):
    
    def test_tokenize_create(self):
        """Test tokenization: create file "data.txt" in "./tmp" """
        code = 'create file "data.txt" in "./tmp"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('create', Tokens.VERB),
            ('file', Tokens.TYPE),
            ('data.txt', Tokens.NAME),
            ('in', Tokens.KEYWORD),
            ('./tmp', Tokens.PATH)
        ]
        self.assertEqual(tokens, expected)

    def test_tokenize_replace(self):
        """Test tokenization: replace "./old.txt" with "./new.txt" """
        # Lexer should identify quoted strings with slashes as PATH
        code = 'replace "./old.txt" with "./new.txt"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('replace', Tokens.VERB),
            ('./old.txt', Tokens.PATH),
            ('with', Tokens.KEYWORD),
            ('./new.txt', Tokens.PATH)
        ]
        self.assertEqual(tokens, expected)

    def test_tokenize_delete(self):
        """Test tokenization: delete "file.log" in "./logs" """
        code = 'delete "file.log" in "./logs"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('delete', Tokens.VERB),
            ('file.log', Tokens.NAME),
            ('in', Tokens.KEYWORD),
            ('./logs', Tokens.PATH)
        ]
        self.assertEqual(tokens, expected)

    def test_tokenize_find(self):
        """Test tokenization: find "pattern" """
        code = 'find "pattern"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('find', Tokens.VERB),
            ('pattern', Tokens.NAME)
        ]
        self.assertEqual(tokens, expected)

if __name__ == '__main__':
    unittest.main()