class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for word in s:
            if word == "(" or word == "{" or word == "[":
                stack.append(word)
            elif stack and word == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and word == "]" and stack[-1] == "[":
                stack.pop()
            elif stack and word == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return True if not stack else False