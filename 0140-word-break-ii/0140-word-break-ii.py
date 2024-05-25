class Solution:
    def wordBreak(self, s, wordDict):
        def backtrack(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [[]]  # list containing an empty list to signify valid segmentation
            
            results = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    for subsentence in backtrack(end):
                        results.append([word] + subsentence)
            
            memo[start] = results
            return results
        
        wordDict = set(wordDict)  # Convert list to set for O(1) look-ups
        memo = {}
        
        sentences = backtrack(0)
        return [" ".join(words) for words in sentences]

# Example usage:
solution = Solution()
print(solution.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))  # ["cats and dog","cat sand dog"]
print(solution.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))  # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
print(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # []
