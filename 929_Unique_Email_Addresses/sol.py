def process(mail: str):
    dogsign = mail.find('@');
    local, domain = mail[:dogsign], mail[dogsign+1:]
    local=local[:local.find('+')].replace(".", "")
    return "".join([local, domain])

class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        return len(set([process(e) for e in emails]))
