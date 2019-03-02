class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        prev = int(-10001)
        res = []
        for i, c in enumerate(S):
            if c == C:
                prev = i
            res.append(i-prev)

        prev = int(10001)
        for i in range(len(S) -1, -1, -1):
            if S[i]==C:
                prev = i
            res[i] = min(res[i], prev-i)
            
            
        return res
