class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = len(set(sentence))
        if s == 26 :
            return True
            
        return False
