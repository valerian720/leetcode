class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ransom_char in list(ransomNote):
            char_index = magazine.find(ransom_char)
            if(char_index == -1):
                return False
            else:
                magazine = magazine.replace(ransom_char, '', 1)
        return True