class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(start, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            for i in range(start, n+1):
                curr.append(i)
                backtracking(i+1, curr)
                curr.pop()
        backtracking(1, [])
        return res
                