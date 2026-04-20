class Solution:

    def encode(self, strs: List[str]) -> str:
        message=""
        for s in strs:
            message+= str(len(s))+"#"+s
        return message

    def decode(self, s: str) -> List[str]:
        strs =[]
        i =0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])

            strs.append(s[j+1: j+1+length])
            i= length+1+j
        return strs
            

