class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set = set(words)
        memo = {}
        
        def canForm(word: str) -> bool:
            # If we already calculated the result for this substring, return it
            if word in memo:
                return memo[word]
            
            # Check every possible split point for the current substring
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]
                
                # Condition 1: The prefix itself is a valid word in our set
                if prefix in word_set:
                    # Condition 2: The suffix is either also a valid word, 
                    # or it can be further broken down recursively
                    if suffix in word_set or canForm(suffix):
                        memo[word] = True
                        return True
            
            memo[word] = False
            return False
        
        result = []
        for word in words:
            if not word: 
                continue
            # Temporarily remove the word so it doesn't match itself
            word_set.remove(word)
            
            if canForm(word):
                result.append(word)
                
            # Add it back for subsequent words to use as a building block
            word_set.add(word)
            
        return result