import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add 'src' to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Lexer.language import TokenTypes
from commands.file_ops import (
    CreateCommand, 
    ReplaceCommand, 
    DeleteCommand, 
    FindCommand, 
    GoCommand,
    HelpCommand,
    CurdirCommand
)

class TestCommands(unittest.TestCase):

    # --- CREATE COMMAND TESTS ---
    def test_create_file_validate_success(self):
        # create file "test.txt"
        tokens = [
            ('create', TokenTypes.VERB),
            ('file', TokenTypes.TYPE),
            ('test.txt', TokenTypes.NAME)
        ]
        cmd = CreateCommand(tokens)
        self.assertTrue(cmd.validate())
        self.assertEqual(cmd.path, '.') # default path

    def test_create_file_execute(self):
        tokens = [('create', TokenTypes.VERB), ('file', TokenTypes.TYPE), ('test.txt', TokenTypes.NAME)]
        cmd = CreateCommand(tokens)
        
        # Mock the utility function 'create_file' inside file_ops
        with patch('commands.file_ops.create_file') as mock_create:
            mock_create.return_value = True
            result = cmd.execute()
            
            mock_create.assert_called_with('.', 'test.txt')
            self.assertIn("CREATE file test.txt", result)

    # --- REPLACE COMMAND TESTS ---
    def test_replace_validate_success(self):
        # replace "old.txt" with "new.txt"
        tokens = [
            ('replace', TokenTypes.VERB),
            ('old.txt', TokenTypes.PATH),
            ('with', TokenTypes.KEYWORD),
            ('new.txt', TokenTypes.PATH)
        ]
        cmd = ReplaceCommand(tokens)
        self.assertTrue(cmd.validate())

    @patch('builtins.open')
    @patch('commands.file_ops.smart_move')
    def test_replace_execute(self, mock_move, mock_open):
        tokens = [
            ('replace', TokenTypes.VERB),
            ('old.txt', TokenTypes.PATH),
            ('with', TokenTypes.KEYWORD),
            ('new.txt', TokenTypes.PATH)
        ]
        cmd = ReplaceCommand(tokens)
        
        # Mock reading the old file
        mock_file = MagicMock()
        mock_file.read.return_value = "file_content"
        mock_open.return_value = mock_file
        
        mock_move.return_value = True
        
        result = cmd.execute()
        self.assertIn("REPLACE old.txt WITH new.txt", result)
        mock_move.assert_called_with('new.txt', "file_content")

    # --- DELETE COMMAND TESTS ---
    def test_delete_validate_success(self):
        # delete "trash.txt"
        tokens = [
            ('delete', TokenTypes.VERB),
            ('trash.txt', TokenTypes.NAME)
        ]
        cmd = DeleteCommand(tokens)
        self.assertTrue(cmd.validate())

    @patch('commands.file_ops.delete_dir')
    def test_delete_execute(self, mock_delete):
        tokens = [('delete', TokenTypes.VERB), ('trash.txt', TokenTypes.NAME)]
        cmd = DeleteCommand(tokens)
        
        mock_delete.return_value = True
        result = cmd.execute()
        
        mock_delete.assert_called_with('.')
        self.assertIn("DELETE trash.txt", result)

    # --- FIND COMMAND TESTS ---
    def test_find_validate_success(self):
        # find "pattern" "."
        tokens = [
            ('find', TokenTypes.VERB),
            ('pattern', TokenTypes.NAME),
            ('.', TokenTypes.PATH),
            ('extra', TokenTypes.KEYWORD) 
        ]
        cmd = FindCommand(tokens)
        self.assertTrue(cmd.validate())

    @patch('commands.file_ops.scan_directory')
    def test_find_execute(self, mock_scan):
        tokens = [
            ('find', TokenTypes.VERB),
            ('pattern', TokenTypes.NAME),
            ('.', TokenTypes.PATH),
            ('dummy', TokenTypes.KEYWORD)
        ]
        cmd = FindCommand(tokens)
        mock_scan.return_value = 5 # 5 items found
        
        result = cmd.execute()
        self.assertIn("FOUND 5 items matching pattern", result)

    # --- GO COMMAND TESTS ---
    def test_go_validate(self):
        # go "C:/Users"
        tokens = [('go', TokenTypes.VERB), ('C:/Users', TokenTypes.PATH)]
        cmd = GoCommand(tokens)
        self.assertTrue(cmd.validate())

    @patch('commands.file_ops.go')
    def test_go_execute(self, mock_go):
        tokens = [('go', TokenTypes.VERB), ('C:/Users', TokenTypes.PATH)]
        cmd = GoCommand(tokens)
        mock_go.return_value = "you went to: C:/Users"
        
        result = cmd.execute()
        self.assertEqual(result, "you went to: C:/Users")

    # --- HELP COMMAND TESTS ---
    def test_help_validate(self):
        tokens = [('help', TokenTypes.VERB)]
        cmd = HelpCommand(tokens)
        self.assertTrue(cmd.validate())

    def test_help_execute(self):
        tokens = [('help', TokenTypes.VERB)]
        cmd = HelpCommand(tokens)
        result = cmd.execute()
        self.assertIn("Available Commands", result)
        self.assertIn("CURDIR", result)

    # --- CURDIR COMMAND TESTS ---
    def test_curdir_validate(self):
        tokens = [('curdir', TokenTypes.VERB)]
        cmd = CurdirCommand(tokens)
        self.assertTrue(cmd.validate())

    @patch('os.getcwd')
    def test_curdir_execute(self, mock_getcwd):
        tokens = [('curdir', TokenTypes.VERB)]
        cmd = CurdirCommand(tokens)
        
        mock_getcwd.return_value = "/home/user/project"
        result = cmd.execute()
        
        self.assertEqual(result, "Current Directory: /home/user/project")

if __name__ == '__main__':
    unittest.main()