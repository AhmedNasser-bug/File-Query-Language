import re

class Vlaid:
    @staticmethod
    def path(path):
        """Validate if path follows correct format"""
        return Vlaid.is_path(path)
    
    @staticmethod
    def is_path(token):
        """
        Check if token is a path.
        Valid paths:
        - ~/folder/folder
        - [partition]://folder/folder
        - ~/[partition]://folder/folder
        - /folder/folder
        """
        # Path patterns: contains / or ~ or ://
        path_pattern = r'^(~|[a-zA-Z0-9]+:\/\/|~\/[a-zA-Z0-9]+:\/\/)(\/)?([a-zA-Z0-9_\-]+\/)*([a-zA-Z0-9_\-]+)?$|^\/([a-zA-Z0-9_\-]+\/)*([a-zA-Z0-9_\-]+)?$'
        
        if re.match(path_pattern, token):
            return True
        return False
    
    @staticmethod
    def validate_verb(token):
        """Validate if token is a valid VERB"""
        valid_verbs = ["CREATE", "REPLACE", "FIND", "DELETE"]
        return token.upper() in valid_verbs
    
    @staticmethod
    def validate_name(token):
        """Validate if token is a valid file/folder name"""
        # File names: alphanumeric, underscore, hyphen (no spaces)
        name_pattern = r'^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)?$'
        return re.match(name_pattern, token) is not None