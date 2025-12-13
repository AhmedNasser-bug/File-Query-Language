import unittest
import sys
import os

# Add 'src' to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from parser import Parser
from Lexer.language import TokenTypes
from commands.file_ops import (
    CreateCommand, 
    DeleteCommand, 
    ReplaceCommand, 
    FindCommand, 
    GoCommand, 
    HelpCommand, 
    CurdirCommand
)

class TestParser(unittest.TestCase):

    def test_parse_create_command(self):
        """Validate CREATE tokens -> CreateCommand object"""
        tokens = [
            ('create', TokenTypes.VERB),
            ('file', TokenTypes.TYPE),
            ('data.txt', TokenTypes.NAME),
            ('in', TokenTypes.KEYWORD),
            ('./tmp', TokenTypes.PATH)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        
        self.assertIsInstance(command, CreateCommand)
        self.assertEqual(command.path, './tmp')
        self.assertEqual(command.data, 'data.txt')

    def test_parse_replace_command(self):
        """Validate REPLACE tokens -> ReplaceCommand object"""
        tokens = [
            ('replace', TokenTypes.VERB),
            ('./old.txt', TokenTypes.PATH),
            ('with', TokenTypes.KEYWORD),
            ('./new.txt', TokenTypes.PATH)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        
        self.assertIsInstance(command, ReplaceCommand)
        self.assertEqual(command.OldPath, './old.txt')
        self.assertEqual(command.NewPath, './new.txt')

    def test_parse_delete_command(self):
        """Validate DELETE tokens -> DeleteCommand object"""
        tokens = [
            ('delete', TokenTypes.VERB),
            ('file.log', TokenTypes.NAME),
            ('in', TokenTypes.KEYWORD),
            ('./logs', TokenTypes.PATH)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        
        self.assertIsInstance(command, DeleteCommand)
        self.assertEqual(command.data, 'file.log')
        self.assertEqual(command.path, './logs')

    def test_parse_find_command(self):
        """Validate FIND tokens -> FindCommand object"""
        tokens = [
            ('find', TokenTypes.VERB),
            ('pattern', TokenTypes.NAME),
            ('./', TokenTypes.PATH),
            ('x', TokenTypes.KEYWORD)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        print("*******************", command.data)
        self.assertIsInstance(command, FindCommand)
        self.assertEqual(command.data, 'pattern')

    def test_parse_go_command(self):
        """Validate GO tokens -> GoCommand object"""
        tokens = [
            ('go', TokenTypes.VERB),
            ('../', TokenTypes.PATH)
        ]
        parser = Parser(tokens)
        command = parser.parse()
        self.assertIsInstance(command, GoCommand)
        self.assertEqual(command.path, '../')

    def test_parse_help_command(self):
        """Validate HELP tokens -> HelpCommand object"""
        tokens = [('help', TokenTypes.VERB)]
        parser = Parser(tokens)
        command = parser.parse()
        self.assertIsInstance(command, HelpCommand)

    def test_parse_curdir_command(self):
        """Validate CURDIR tokens -> CurdirCommand object"""
        tokens = [('curdir', TokenTypes.VERB)]
        parser = Parser(tokens)
        command = parser.parse()
        self.assertIsInstance(command, CurdirCommand)

if __name__ == '__main__':
    unittest.main()