class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for s in strs:  
            count = [0]*26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')]+=1
            anagrams_dict.setdefault(tuple(count),[]).append(s)

        return list(anagrams_dict.values())