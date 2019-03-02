class Solution {
public:
    vector<int> shortestToChar(string S, char C) {
        auto prev = -10001;
        vector<int> res;
        for(int i=0; i < S.size(); i++){
            if (S[i]==C)
                prev = i;
            res.push_back(i - prev);
        }
        
        prev = 10001;
        for(int i=S.size()-1; i>=0; i--){
            if (S[i]==C)
                prev = i;
            res[i] = std::min(res[i], prev - i);
        }
        
        return res;
    }
};
