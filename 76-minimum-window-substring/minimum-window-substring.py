class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        have_count = 0
        need_count = len(need)

        window = Counter()
        res_l = 0
        res_r = float("inf")

        l = 0

        for r, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                have_count += 1

            while have_count == need_count:
                if (r - l + 1) < (res_r - res_l + 1):
                    res_r, res_l = r, l

                left_ch = s[l] # char at left pointer
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have_count -= 1
                
                l += 1

        if res_r == float("inf"): 
            return ""
        else:
            return s[res_l:res_r+1]


      