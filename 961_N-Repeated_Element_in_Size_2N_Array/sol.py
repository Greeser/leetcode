class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = collections.Counter(A)
        for c in counter:
            if counter[c] > 1:
                return c
        
