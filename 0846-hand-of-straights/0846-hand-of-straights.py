from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        sorted_keys = sorted(count)
        
        for key in sorted_keys:
            if count[key] > 0:
                num_needed = count[key]
                for i in range(groupSize):
                    if count[key + i] < num_needed:
                        return False
                    count[key + i] -= num_needed
        
        return True

# Example usage:
solution = Solution()
print(solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # Output: True
print(solution.isNStraightHand([1,2,3,4,5], 4))          # Output: False
