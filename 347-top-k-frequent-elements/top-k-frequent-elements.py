class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
                continue
                
            freq[num] += 1

        heap = [] # min heap by default

        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            
            if len(heap) > k:
                heapq.heappop(heap)

        elements = [value for _, value in heap]
        
        return list(elements)


            