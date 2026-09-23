from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        #return sorted(count.items(), key = lambda a, b : b, reverse=True)[:k]
        #return [num for num, freq in count.most_common(k)]
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        res = []

        for freq in range(len(bucket)-1, 0, -1):
            res.extend(bucket[freq])
            if len(res) >= k :
                return res[:k]
