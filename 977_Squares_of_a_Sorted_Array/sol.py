class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([pow(x,2) for x in A])
        
