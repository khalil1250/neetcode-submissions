from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for char in strs:
            s_char = ''.join(sorted(char))
            if s_char in words:
                words[s_char].append(char)
            else:
                words[s_char] = [char]

        values = list(words.values())
        return values