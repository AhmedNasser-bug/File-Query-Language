#include <iostream>
#include <vector>
#include <string>

// C-compatible interface for Python ctypes
extern "C" {
    
    // Example function: Returns 1 if pattern found, 0 otherwise
    int fast_scan(const char* root_dir, const char* pattern) {
        std::string dir(root_dir);
        std::string pat(pattern);
        
        // TODO: Implement std::filesystem traversal
        std::cout << "[C++] Scanning " << dir << " for " << pat << std::endl;
        return 1;
    }
}
