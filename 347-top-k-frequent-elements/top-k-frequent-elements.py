class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hash map where key is the integer, value is the frequency
        count = {}

        nums_heap = [] # min-heap by default

        for num in nums:
            if num in count: # check if num is a key in count
                count[num] = count[num] + 1 # increment frequency
            else:
                count[num] = 1

        # for key, value in hashmap items
        for num, freq in count.items(): # .items() gives (key, value) pairs
            # use (freq, num) as heapq uses first value in tuples to compare
            heapq.heappush(nums_heap, (freq, num))
            if len(nums_heap) > k:
                # min-heap pop removes smallest element
                heapq.heappop(nums_heap) # so we are left with top k
        
        return [num for (freq, num) in nums_heap] # return nums as a list
        


