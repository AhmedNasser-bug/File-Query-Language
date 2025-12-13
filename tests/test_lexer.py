'''
Docstring for tests.test_lexer

This module contains unit tests for the Lexer class in src.Lexer.lexer.
It verifies that various input commands are tokenized correctly.
'''

import unittest
import sys
import os

# Add 'src' to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from Lexer.lexer import Lexer
from Lexer.language import Tokens
