class Solution:
    
    @staticmethod
    def word_to_hash(word):
        counts = {}

        for char in word:
            counts[char] = counts.get(char, 0) + 1

        return tuple(sorted(counts.items()))

    def groupAnagrams(self, strs):
        grouped_map = defaultdict(list)

        for word in strs:
            key = self.word_to_hash(word)
            grouped_map[key].append(word)

        return list(grouped_map.values())
        