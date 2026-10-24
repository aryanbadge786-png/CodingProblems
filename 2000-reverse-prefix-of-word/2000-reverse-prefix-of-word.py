class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        for i in range(len(word)):
            if ch == word[i]:
                index = i
                break
        if index == -1:
            return word
        prefix = word[0:index+1]
        revprefix = prefix[ : : -1]
        last = word[index+1:]
        ans = revprefix + last
        return ans