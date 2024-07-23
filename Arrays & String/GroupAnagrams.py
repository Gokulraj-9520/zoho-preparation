class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word]=[word]
        result= list(anagrams.values())
        for group in result:
            group.sort()
        result.sort(key=lambda x: (len(x), x))
        return result