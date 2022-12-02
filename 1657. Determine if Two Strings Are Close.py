# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         ret = True
#         # 
#         if(len(word1) != len(word2)):
#           ret = False
#         # 
#         if(set(word1) != set(word2)):
#           ret = False
#         # 
#         nums1 = {x:list(word1).count(x) for x in set(word1)}.values()
#         nums2 = {x:list(word2).count(x) for x in set(word2)}.values()
#         if(sorted(nums1) != sorted(nums2)):
#           ret = False
#         return ret;

class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        return sorted(Counter(w1).values()) == sorted(Counter(w2).values()) \
               and set(w1) == set(w2)