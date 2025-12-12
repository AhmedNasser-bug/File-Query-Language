import re


def validate_path(path_str: str) -> bool:
    """
    Validates the syntax of a file path for the FQL interpreter.
    
    Accepts:
    - Standard paths: 'folder/file'
    - Drive letters: 'C:/folder' or 'C://'
    - Tilde expansion: '~/folder'
    - Mixed Tilde+Drive: '~/C:/folder' (as requested)
    - Duplicate slashes: 'folder//subfolder' (common user input error, usually valid in OS)
    """
    if not isinstance(path_str, str) or not path_str.strip():
        return False
    
    # REGEX BREAKDOWN:
    # 1. ^                      : Start of string
    # 2. (?:[\\/]+)?           : OPTIONAL Tilde start (matches "/" or "~\")
    # 3. (?:[a-zA-Z]:[\\/]+)?   : OPTIONAL Drive start (matches "C:/" or "D:\")
    # 4. (?:[\\/]+)?            : OPTIONAL Root slash (matches "/" if no drive letter is present)
    # 5. (?:[\w\s\-\.]+[\\/]) : PATH BODY (Repeated groups of names allowed charaters)
    #                             Allowed: Alphanumeric, spaces, dashes, dots.
    #                             Followed by optional separators.
    # 6. $                      : End of string
    
    pattern = r'^(?:~[\\/]+)?(?:[a-zA-Z]:[\\/]+|(?:[\\/]+))?(?:[\w\s\-\.]+[\\/])$'
    
    return bool(re.match(pattern, path_str))

def validate_filename(name_str: str) -> bool:
    """
    Validates if input is a string and a valid filename (not a path).
    Ensures no path separators or illegal characters are present.
    """
    
    if not isinstance(name_str, str):
        return False
        
    # 2. Check for empty string or purely whitespace
    if not name_str.strip():
        return False

    # 3. Regex to ban illegal characters (Windows is the strictest)
    # Forbidden: < > : " / \ | ? *
    illegal_pattern = r'[<>:"/\\|?*]'
    if re.search(illegal_pattern, name_str):
        return False

    return True

def is_string(token):
    """Check if token is a string enclosed in single or double quotes."""
    string_pattern = r"^(['\"])(.*?)(\1)$"
    return re.match(string_pattern, token) is not None

def validate_verb(token):
    """Validate if token is a valid VERB"""
    valid_verbs = ["create", "replace", "find", "delete","go"]
    return token in valid_verbs

def validate_type(token):
    """Validate if token is a valid TYPE"""
    valid_types = ["file", "folder"]
    return token in valid_types

def validate_keyword(token):
    """Validate if token is a valid KEYWORD"""
    valid_keywords = ["in", "where", "from", "with"]
    return token in valid_keywords