class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()

        s_no_space = s_lower.replace(" ", "")

        s_no_punc = ""

        for char in s_no_space:
            if char.isalnum():
                s_no_punc += char  

        if s_no_punc == s_no_punc[::-1]:
            return True
        else:
            return False    

    