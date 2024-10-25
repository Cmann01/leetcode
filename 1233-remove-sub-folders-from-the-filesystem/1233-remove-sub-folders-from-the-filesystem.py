from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders lexicographically
        folder.sort()
        result = []
        
        # Iterate through each folder path
        for f in folder:
            # If result is empty or the current folder is not a sub-folder of the last added folder in result
            if not result or not f.startswith(result[-1] + "/"):
                result.append(f)
        
        return result
