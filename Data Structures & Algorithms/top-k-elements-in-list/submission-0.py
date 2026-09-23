from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        #sorted(count.items(), key = lambda a, b : b, reverse=True)[:k]
        return [num for num, freq in count.most_common(k)]
