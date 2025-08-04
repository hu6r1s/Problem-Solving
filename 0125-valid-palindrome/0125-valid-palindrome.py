class Solution:
    """
    1. 문자열을 반복문을 돌며 isdigit() or isalpha()이 True라면 string에 붙이기
    반복문이 끝나면 소문자로 모두 변경하고 뒤집은 문자와 같으면 True 반환 
    """
    def isPalindrome(self, s: str) -> bool:
        string = ""
        
        for i in s:
            if i.isdigit() or i.isalpha():
                string += i
        string = string.lower()
        return True if string == string[::-1] else False