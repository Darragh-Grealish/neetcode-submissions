import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s)
        s2 = s2.lower()
        print(s2)
        s1 = s2[::-1]
        if s2 == s1:
            return True
        else:
            return False