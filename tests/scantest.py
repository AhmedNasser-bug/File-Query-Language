import os
import time
import tempfile
import shutil

class ScandirStressTest:
    def __init__(self, depth=5, width=10):
        """
        depth: How many folders deep to nest.
        width: How many files/folders per level.
        Total items ~ width^depth (exponential growth, be careful!)
        """
        self.depth = depth
        self.width = width
        self.temp_dir = tempfile.mkdtemp(prefix="fql_stress_test_")
        self.total_files_created = 0

    def setup(self):
        print(f"--- 1. Generating File Structure ({self.temp_dir}) ---")
        print(f"Target: Depth {self.depth}, Width {self.width}")
        start_time = time.perf_counter()
        
        self._create_tree(self.temp_dir, current_depth=0)
        
        duration = time.perf_counter() - start_time
        print(f"Done. Created {self.total_files_created:,} items in {duration:.4f}s.")

    def _create_tree(self, current_path, current_depth):
        if current_depth >= self.depth:
            return

        # Create files
        for i in range(self.width):
            # Create a dummy file
            with open(os.path.join(current_path, f"file_{i}.txt"), 'w') as f:
                f.write("content")
            self.total_files_created += 1

        # Create subdirectories (Recurse)
        # We limit recursion width to 2 to prevent exploding the hard drive
        # (Total items can get into millions quickly otherwise)
        sub_dirs = 2 if current_depth < self.depth - 1 else 0
        
        for i in range(sub_dirs):
            dir_path = os.path.join(current_path, f"folder_{i}")
            os.makedirs(dir_path)
            self._create_tree(dir_path, current_depth + 1)

    def run_benchmark(self):
        print(f"\n--- 2. Stress Testing os.scandir ---")
        
        start_time = time.perf_counter()
        scanned_count = self._recursive_scandir(self.temp_dir)
        end_time = time.perf_counter()
        
        duration = end_time - start_time
        files_per_sec = scanned_count / duration if duration > 0 else 0
        
        print(f"Scanned Items: {scanned_count:,}")
        print(f"Time Taken:    {duration:.6f} seconds")
        print(f"Speed:         {files_per_sec:,.0f} items/sec")

    def _recursive_scandir(self, path):
        count = 0
        try:
            # The Core Logic: Using os.scandir as a context manager
            with os.scandir(path) as it:
                for entry in it:
                    count += 1
                    if entry.is_dir(follow_symlinks=False):
                        count += self._recursive_scandir(entry.path)
        except PermissionError:
            pass # Standard handling for system files
        return count

    def cleanup(self):
        print(f"\n--- 3. Cleanup ---")
        print("Removing temporary files...")
        shutil.rmtree(self.temp_dir)
        print("Cleanup complete.")

if __name__ == "__main__":
    # Settings: Depth 10 is quite deep; Width 100 ensures high volume per folder.
    # Adjust these numbers to increase/decrease "stress".
    test = ScandirStressTest(depth=10, width=100)
    
    try:
        test.setup()
        test.run_benchmark()
    finally:
        test.cleanup()