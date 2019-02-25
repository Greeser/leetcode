string process(string& email){
    auto dogsign = email.find("@");
    string local = email.substr(0, dogsign);
    local = local.substr(0, local.find("+"));
    local.erase(std::remove(local.begin(), local.end(), '.'), local.end());
    string domain = email.substr(dogsign);
    return local+domain;
}

class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        std::transform(emails.begin(), emails.end(), emails.begin(), process);
        std::set<string> s(emails.begin(), emails.end());
        return s.size();
    }
};
