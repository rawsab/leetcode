class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        elements = set()
        for num in nums:
            elements.add(num)

        max_res = 0

        for e in elements:
            if e - 1 in elements:
                continue
                
            current_res = 1
            temp = e + 1
            while temp in elements:
                current_res += 1
                temp += 1

            max_res = max(max_res, current_res)

        return max_res
        