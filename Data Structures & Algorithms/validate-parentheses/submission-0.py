class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = set('({[')
        closes = set(')}]')
        mapp = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in opens:
                stack.append(char)
            if char in closes:
                if stack and stack[-1] == mapp[char]:
                    stack = stack[:-1]
                else:
                    # either stack is empty
                    # or last inserted character is not a opening bracket for the current closing one
                    return False
        # If the opening and closing pair is matching, then we should now have an empty stack
        return not stack