from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # BFS to build parent graph
        parents = defaultdict(set)
        current_level = {beginWord}
        visited = {beginWord}
        found = False

        while current_level and not found:
            next_level = set()
            for word in current_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nw = word[:i] + c + word[i+1:]
                        if nw in wordSet and nw not in visited:
                            next_level.add(nw)
                            parents[nw].add(word)
                            if nw == endWord:
                                found = True
            visited |= next_level
            current_level = next_level

        if not found:
            return []

        # Backtrack from endWord to beginWord
        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append(list(reversed(path)))
                return
            for parent in parents[word]:
                path.append(parent)
                backtrack(parent, path)
                path.pop()

        backtrack(endWord, [endWord])
        return res