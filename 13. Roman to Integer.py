class Solution:
    def romanToInt(self, s: str) -> int:
        rom_numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        return sum([rom_numbers[s[i]] * (1 if rom_numbers[s[i]] >= rom_numbers[s[i+1]] else -1) for i in range(len(s)-1)]) + rom_numbers[s[-1:]]