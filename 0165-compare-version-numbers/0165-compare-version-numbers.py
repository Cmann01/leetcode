class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_revisions = version1.split('.')  
        v2_revisions = version2.split('.') 
        
        
        i = 0
        while i < max(len(v1_revisions), len(v2_revisions)):
            v1 = int(v1_revisions[i]) if i < len(v1_revisions) else 0
            v2 = int(v2_revisions[i]) if i < len(v2_revisions) else 0
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            else:
                i += 1  
        
        return 0  

solution = Solution()
print(solution.compareVersion("1.01", "1.001"))  # Output: 0
print(solution.compareVersion("1.0", "1.0.0"))   # Output: 0
print(solution.compareVersion("0.1", "1.1"))     # Output: -1
