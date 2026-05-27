from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_collect = defaultdict(list)
        result = []

        for i in strs:
            j = tuple(sorted(i))
            anagram_collect[j].append(i)

        for values in anagram_collect.values():
            result.append(values)

        return result    