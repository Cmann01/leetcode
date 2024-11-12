from typing import List
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price first. If prices are the same, keep the item with max beauty.
        items.sort()
        
        # Create lists for prices and cumulative max beauty.
        prices = []
        max_beauty = []
        
        current_max_beauty = 0
        for price, beauty in items:
            if not prices or price != prices[-1]:
                # Add new price only if it hasn't been added before
                prices.append(price)
                current_max_beauty = max(current_max_beauty, beauty)
                max_beauty.append(current_max_beauty)
            else:
                # Update max_beauty with the highest beauty for the same price
                current_max_beauty = max(current_max_beauty, beauty)
                max_beauty[-1] = current_max_beauty
        
        # Process each query
        result = []
        for query in queries:
            # Use binary search to find the rightmost price <= query
            idx = bisect_right(prices, query) - 1
            if idx == -1:
                # No price is less than or equal to the query
                result.append(0)
            else:
                # Append the maximum beauty up to this price
                result.append(max_beauty[idx])
        
        return result
