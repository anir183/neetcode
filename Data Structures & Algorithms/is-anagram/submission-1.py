class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)

        if not sl == tl:
            return False
        
        alphs = {}
        for i in range(sl):
            sc = s[i]
            tc = t[i]

            if not sc in alphs:
                alphs[sc] = 0

            if not tc in alphs:
                alphs[tc] = 0

            alphs[sc] = alphs[sc] + 1
            alphs[tc] = alphs[tc] - 1
        
        for _, val in alphs.items():
            if not val == 0:
                return False
        
        return True