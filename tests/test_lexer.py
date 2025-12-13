import unittest
import sys
import os

# Add 'src' to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Lexer.lexer import Lexer
from Lexer.language import TokenTypes

class TestLexer(unittest.TestCase):
    
    def test_tokenize_create(self):
        """Test tokenization: create file "data.txt" in "./tmp" """
        code = 'create file "data.txt" in "./tmp"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('create', TokenTypes.VERB),
            ('file', TokenTypes.TYPE),
            ('data.txt', TokenTypes.NAME),
            ('in', TokenTypes.KEYWORD),
            ('./tmp', TokenTypes.PATH)
        ]
        self.assertEqual(tokens, expected)

    def test_tokenize_replace(self):
        """Test tokenization: replace "./old.txt" with "./new.txt" """
        code = 'replace "./old.txt" with "./new.txt"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('replace', TokenTypes.VERB),
            ('./old.txt', TokenTypes.PATH),
            ('with', TokenTypes.KEYWORD),
            ('./new.txt', TokenTypes.PATH)
        ]
        self.assertEqual(tokens, expected)

    def test_tokenize_delete(self):
        """Test tokenization: delete "file.log" in "./logs" """
        code = 'delete "file.log" in "./logs"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('delete', TokenTypes.VERB),
            ('file.log', TokenTypes.NAME),
            ('in', TokenTypes.KEYWORD),
            ('./logs', TokenTypes.PATH)
        ]
        self.assertEqual(tokens, expected)

    def test_tokenize_find(self):
        """Test tokenization: find "pattern" """
        code = 'find "pattern"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('find', TokenTypes.VERB),
            ('pattern', TokenTypes.NAME)
        ]
        self.assertEqual(tokens, expected)

    def test_tokenize_go(self):
        """Test tokenization: go "C:/users" """
        code = 'go "C:/users"'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected = [
            ('go', TokenTypes.VERB),
            ('C:/users', TokenTypes.PATH)
        ]
        self.assertEqual(tokens, expected)

    def test_tokenize_help(self):
        """Test tokenization: help"""
        code = 'help'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        expected = [('help', TokenTypes.VERB)]
        self.assertEqual(tokens, expected)

    def test_tokenize_curdir(self):
        """Test tokenization: curdir"""
        code = 'curdir'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        expected = [('curdir', TokenTypes.VERB)]
        self.assertEqual(tokens, expected)

if __name__ == '__main__':
    unittest.main()