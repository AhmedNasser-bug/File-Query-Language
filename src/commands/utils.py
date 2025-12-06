'''
Docstring for src.commands.utils

This module provides utility functions for command processing.
'''
import os
import json
from ripgrepy import Ripgrepy

def scan_directory(path: str, pattern: str) -> int:
    """
    Uses ripgrep to scan for files containing 'pattern'.
    """
    try:
        # 1. Setup the search
        # - .json(): Get results as structured data
        # - .with_filename(): Ensure we get file paths
        # - .line_number(): (Optional) Get line numbers
        rg = Ripgrepy(pattern, path).json().with_filename()

        # 2. Run the search
        result_json = rg.run().as_string
        
        # 3. Parse Results
        # Ripgrep returns JSON lines. We parse them to count matches.
        count = 0
        if result_json:
            lines = result_json.strip().split('\n')
            for line in lines:
                data = json.loads(line)
                if data['type'] == 'match':
                    # Print match like your C++ code did
                    file_path = data['data']['path']['text']
                    print(file_path) 
                    count += 1
                    
        return count

    except Exception as e:
        print(f"[Error] Ripgrep failed: {e}")
        return 0

def create_file(path: str, content: str = ""):
    """
    Creates a new file (or overwrites) and writes content.
    Uses low-level file descriptors.
    """
    # Flags: Write Only | Create if missing | Truncate (overwrite) if exists
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    
    # 0o644 = Read/Write for owner, Read for others (standard permission)
    fd = os.open(path, flags, 0o644)

    if content:
        os.write(fd, content.encode('utf-8'))
    os.close(fd)
    return 1

def delete_dir(path: str):
    """
    Recursively deletes a directory and all its contents (files/subdirs).
    Strict 'os' module implementation (Bottom-Up Walk).
    """

    # Walk bottom-up (files first, then folders)
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    
    # Finally, remove the root folder itself
    os.rmdir(path)

import os
import shutil

def smart_move(src: str, dst: str) -> str:
    """    
    Logic:
    1. If 'dst' is an existing DIRECTORY -> Moves 'src' INTO 'dst'.
    2. If 'dst' is a FILE path (or doesn't exist) -> Renames/Moves 'src' TO 'dst'.
    3. If 'dst' file already exists -> Silently overwrites it (Force Replace).
    
    Returns: A success message string.
    """
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source file '{src}' not found.")

    # 1. Resolve the real destination path
    real_dst = dst
    if os.path.isdir(dst):
        # If dst is a folder, append the src filename (e.g., "folder/" -> "folder/file.txt")
        src_name = os.path.basename(src)
        real_dst = os.path.join(dst, src_name)

    # 2. Check for Overwrite (Critical for Windows)
    # Windows fails if you try to move a file to a path that exists.
    # We must remove the destination first to simulate a "REPLACE" command.
    if os.path.exists(real_dst) and os.path.isfile(real_dst):
        # Don't delete if we are just moving the file to itself (case insensitivity check)
        if os.path.abspath(src).lower() != os.path.abspath(real_dst).lower():
            os.remove(real_dst)

    # 3. Perform the Move
    try:
        shutil.move(src, real_dst)
        return f"Moved '{src}' -> '{real_dst}'"
    except OSError as e:
        raise OSError(f"Failed to move/replace '{src}': {e}")