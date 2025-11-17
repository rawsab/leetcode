class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        
        res = 0
        curr_seen = set()
        l = 0

        for r in range(len(s)):

            if s[r] in curr_seen:
                while l < r and s[r] in curr_seen:
                    curr_seen.remove(s[l])
                    l += 1
                    
            curr_seen.add(s[r])
            res = max(res, r - l + 1)
        
        return res