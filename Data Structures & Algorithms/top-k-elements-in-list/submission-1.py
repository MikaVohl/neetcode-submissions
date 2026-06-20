
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        heap = []
        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        out = []
        for i in range(k):
            out.append(heapq.heappop(heap)[1])
        return out