# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    def match(self, word_list):
        sorted_word = sorted(self.word)
        anagrams = [word for word in word_list if sorted(word.lower()) == sorted_word and word.lower() != self.word]

        return anagrams
