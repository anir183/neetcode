class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)

        if not sl == tl:
            return False
        
        alphs = {}

        for char in s:
            alphs[char] = alphs.get(char, 0) + 1
        
        for char in t:
            if char not in alphs:
                return False
            
            alphs[char] -= 1

            if alphs[char] < 0:
                return False
        
        return True