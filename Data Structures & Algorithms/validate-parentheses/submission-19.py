class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for i in range(0, len(s)):
            if s[i] in ('[', '{', '('):
                a.append(s[i])
            else:
                if not a:
                    return False
                top = a[-1]
                if s[i] == ']' and top == '[':
                    a.pop()
                elif s[i] == '}' and top == '{':
                    a.pop()
                elif s[i] == ')' and top == '(':
                    a.pop()
                else:
                    return False
        return len(a) == 0