class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        std::transform(A.begin(), A.end(), A.begin(), [](int c){ return c*c; });
        std::sort(A.begin(), A.end());
        return A;
        
    }
};
