class Solution:
    def isAlphaNum(self, char) -> bool:
        is_alpha = (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90)
        is_num = 48 <= ord(char) <= 57
        return is_alpha or is_num

    def isPalindrome(self, s: str) -> bool:

        """
            Brute:
                remove the non alpha num and reverse the string, 
                store and compare
                T/S: O(N)/O(N)
            
            Optimal:
                Two pointers, left and right on the s.
                Check isAlphaNum and move the pointers
                accordingly
                T/S: O(N)/O(1)
        """
        # Brute
        rev = ""
        for char in s.lower():
            if self.isAlphaNum(char): rev += char
        return rev == rev[::-1]
        
        # Optimal
        # left = 0
        # right = len(s) - 1

        # while left < right:

        #     if not self.isAlphaNum(s[left]): left += 1
        #     elif not self.isAlphaNum(s[right]): right -= 1
        #     elif self.isAlphaNum(s[left]) and self.isAlphaNum(s[right]) and str(s[left]).lower() != str(s[right]).lower():
        #         return False
        #     else:
        #         left += 1
        #         right -= 1

        # return True



        