# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word
        self.sorted_word = self.sort_word(word)

    def sort_word(self, word):
        return ''.join(sorted(word))

    def match(self, anagram):
        matches=[]
        for candidate in anagram:
            if self.sort_word(candidate) ==self.sorted_word:
                matches.append(candidate)

        return matches