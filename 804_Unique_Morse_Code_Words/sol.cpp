class Solution {
public:
    vector<string> alphabet = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
    string process(string word){
        vector<string> tmp;
        for(char& c: word){
            tmp.push_back(alphabet[int(c) - 97]);
        }
        std::string result;
        for (auto const& s : tmp) { result += s; }
        return result;
    }
    
    int uniqueMorseRepresentations(vector<string>& words) {
        transform(words.begin(), words.end(), words.begin(), [this](string& s){
            return process(s);
        });
        std::set<string> s(words.begin(), words.end());
        return s.size();
    }
};
