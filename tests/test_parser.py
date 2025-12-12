import unittest
import sys
import os

# Add 'src' to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from parser import Parser
from tokens import Tokens
# Note: Importing 'RepalceCommand' exactly as it appears in the source code (typo preservation)
from commands.file_ops import CreateCommand, DeleteCommand, ReplaceCommand, FindCommand

class TestParser(unittest.TestCase):

    def test_parse_create_command(self):
        """Validate CREATE tokens -> CreateCommand object"""
        tokens = [
            ('create', Tokens.VERB),
            ('file', Tokens.TYPE),
            ('data.txt', Tokens.NAME),
            ('in', Tokens.KEYWORD),
            ('./tmp', Tokens.PATH)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        
        self.assertIsInstance(command, CreateCommand)
        self.assertEqual(command.path, './tmp')
        self.assertEqual(command.data, 'data.txt')

    def test_parse_replace_command(self):
        """Validate REPLACE tokens -> RepalceCommand object"""
        tokens = [
            ('replace', Tokens.VERB),
            ('./old.txt', Tokens.PATH),
            ('with', Tokens.KEYWORD),
            ('./new.txt', Tokens.PATH)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        
        self.assertIsInstance(command, ReplaceCommand)
        self.assertEqual(command.OldPath, './old.txt')
        self.assertEqual(command.NewPath, './new.txt')

    def test_parse_delete_command(self):
        """Validate DELETE tokens -> DeleteCommand object"""
        tokens = [
            ('delete', Tokens.VERB),
            ('file.log', Tokens.NAME),
            ('in', Tokens.KEYWORD),
            ('./logs', Tokens.PATH)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        
        self.assertIsInstance(command, DeleteCommand)
        self.assertEqual(command.data, 'file.log')
        self.assertEqual(command.path, './logs')

    def test_parse_find_command(self):
        """Validate FIND tokens -> FindCommand object"""
        tokens = [
            ('find', Tokens.VERB),
            ('pattern', Tokens.NAME)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        
        self.assertIsInstance(command, FindCommand)
        self.assertEqual(command.data, 'pattern')

if __name__ == '__main__':
    unittest.main()