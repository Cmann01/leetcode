import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Function to calculate the marginal gain
        def gain(passi, totali):
            return (passi + 1) / (totali + 1) - passi / totali
        
        # Max-Heap to store the negative of marginal gain and class info
        heap = []
        for passi, totali in classes:
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))
        
        # Distribute extra students
        for _ in range(extraStudents):
            max_gain, passi, totali = heapq.heappop(heap)
            passi += 1
            totali += 1
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))
        
        # Calculate the final average pass ratio
        total_ratio = 0
        for _, passi, totali in heap:
            total_ratio += passi / totali
        
        return total_ratio / len(classes)
