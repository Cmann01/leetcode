class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        from collections import defaultdict
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = defaultdict(int)
        consonant_count = 0
        left = 0
        result = 0
        
        # Preprocessing to find the index of the next consonant for each position
        n = len(word)
        next_consonant = [n] * n
        last_consonant_idx = n
        
        for i in range(n - 1, -1, -1):
            next_consonant[i] = last_consonant_idx
            if word[i] not in vowels:
                last_consonant_idx = i
        
        for right in range(n):
            if word[right] in vowels:
                vowel_count[word[right]] += 1
            else:
                consonant_count += 1
            
            while consonant_count > k:
                if word[left] in vowels:
                    vowel_count[word[left]] -= 1
                    if vowel_count[word[left]] == 0:
                        del vowel_count[word[left]]
                else:
                    consonant_count -= 1
                left += 1
            
            while left < n and len(vowel_count) == 5 and consonant_count == k:
                idx = next_consonant[right]  # Find the next consonant after `right`
                result += idx - right  # Count all valid substrings ending between `right` and `idx`
                
                if word[left] in vowels:
                    vowel_count[word[left]] -= 1
                    if vowel_count[word[left]] == 0:
                        del vowel_count[word[left]]
                else:
                    consonant_count -= 1
                left += 1
        
        return result