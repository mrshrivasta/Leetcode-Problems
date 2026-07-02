class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())

        exact = set(wordlist)
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            lower = word.lower()

            if lower not in case_map:
                case_map[lower] = word

            dv = devowel(word)
            if dv not in vowel_map:
                vowel_map[dv] = word

        ans = []

        for query in queries:
            if query in exact:
                ans.append(query)
            elif query.lower() in case_map:
                ans.append(case_map[query.lower()])
            elif devowel(query) in vowel_map:
                ans.append(vowel_map[devowel(query)])
            else:
                ans.append("")

        return ans