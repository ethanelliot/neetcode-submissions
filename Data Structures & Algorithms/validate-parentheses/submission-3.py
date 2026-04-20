class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closing ={')':"(", ']':"[", '}':'{'}

        for char in s:
            if char in set(closing.values()):
                stack.append(char)
            else:
                if len(stack)>0 and closing[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return False if len(stack) !=0 else True