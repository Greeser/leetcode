class Solution:
    def __init__(self):
        self.alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
    def process(self, word: str):
        return "".join([self.alphabet[ord(s) - 97] for s in word])
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set([self.process(word) for word in words]))
        
