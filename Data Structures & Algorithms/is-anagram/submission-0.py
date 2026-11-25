class Solution:

    @staticmethod
    def anagram_map(anagram):
        word_count = {}
        for i in anagram:
            if i not in word_count:
                word_count[i] = 1
            word_count[i] += 1
        return word_count

    def isAnagram(self, s: str, t: str) -> bool:
        if self.anagram_map(s) == self.anagram_map(t):
            return True
        return False
        
    