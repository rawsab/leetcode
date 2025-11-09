class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        l, r = 0, minSize
        substrings = {}

        max_freq = 0
        
        while r <= len(s):
            sub = s[l:r]

            if sub in substrings:
                substrings[sub] += 1
            elif len(set(sub)) <= maxLetters:
                substrings[sub] = 1

            max_freq = max(max_freq, substrings.get(sub, 0))

            l = l + 1
            r = r + 1

        return max_freq