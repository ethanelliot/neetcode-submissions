class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_chars = dict()
        t_chars = dict()

        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1

        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1

        for char, count in s_chars.items():
            if t_chars.get(char, -1) != count:
                return False
        return True
        
