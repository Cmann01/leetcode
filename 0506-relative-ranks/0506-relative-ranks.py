class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_scores = sorted(score, reverse=True)
        ranks = {}
        for i in range(len(sorted_scores)):
            if i == 0:
                ranks[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                ranks[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                ranks[sorted_scores[i]] = "Bronze Medal"
            else:
                ranks[sorted_scores[i]] = str(i + 1)
        
        return [ranks[score[i]] for i in range(len(score))]
