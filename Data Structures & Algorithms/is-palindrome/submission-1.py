class Solution:
    def isAlphaNum(self, char) -> bool:
        is_alpha = (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90)
        is_num = 48 <= ord(char) <= 57
        return is_alpha or is_num

    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            if not self.isAlphaNum(s[left]): left += 1
            elif not self.isAlphaNum(s[right]): right -= 1
            elif self.isAlphaNum(s[left]) and self.isAlphaNum(s[right]) and str(s[left]).lower() != str(s[right]).lower():
                return False
            else:
                left += 1
                right -= 1

        return True



        