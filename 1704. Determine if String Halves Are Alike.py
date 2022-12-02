class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        indexes = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
        idexes_keys = indexes.keys()
        half_lengh = len(s)//2
        for i in range(half_lengh): 
            # left part
            if(s[i] in idexes_keys):
                indexes[s[i]] += 1
            # right part
            if(s[half_lengh+i] in idexes_keys):
                indexes[s[half_lengh+i]] -= 1
        return sum(indexes.values()) == 0
