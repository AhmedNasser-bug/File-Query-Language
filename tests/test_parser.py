'''
Docstring for tests.test_parser
This module contains unit tests for the Parser class in src.parser.
It verifies that various token lists are parsed into the correct command objects.
'''

import unittest
import sys
import os

# Add 'src' to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from parser import Parser
from Lexer.language import Language, TokenTypes
# Note: Importing 'RepalceCommand' exactly as it appears in the source code (typo preservation)
from commands.file_ops import CreateCommand, DeleteCommand, ReplaceCommand, FindCommand
