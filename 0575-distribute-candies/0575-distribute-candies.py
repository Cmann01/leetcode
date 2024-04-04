class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        # Calculate the upper limit of the number of kinds of candies sister can gain
        upper_limit = len(candyType) // 2
        unique_candies = set()
        for candy in candyType:
            unique_candies.add(candy)
        return min(len(unique_candies), upper_limit)
