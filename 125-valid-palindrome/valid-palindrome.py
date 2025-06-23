class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left_letter = 0
        right_letter = len(s) - 1
        while left_letter < right_letter:
            if s[left_letter].isalnum() == False:
                left_letter += 1
            elif s[right_letter].isalnum() == False:
                right_letter -= 1
            elif s[left_letter] != s[right_letter]:
                return False
            elif s[left_letter] == s[right_letter]:
                left_letter += 1
                right_letter -= 1
        return True
 
        
