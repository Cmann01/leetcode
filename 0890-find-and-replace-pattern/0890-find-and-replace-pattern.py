class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word, pattern):
            mapping_w = {}
            mapping_p = {}
            for w, p in zip(word, pattern):
                if w not in mapping_w:
                    mapping_w[w] = p
                if p not in mapping_p:
                    mapping_p[p] = w
                if (mapping_w[w], mapping_p[p]) != (p, w):
                    return False
            return True
        
        return [word for word in words if match(word, pattern)]
