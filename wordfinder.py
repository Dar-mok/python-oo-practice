from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        """Creates an instance of the WordFinder class"""
        #self.path = path
        self.words = list(open(f"{path}", "r"))

    def random(self):
        """Return a random word from a list of words"""
        word = choice(self.words)
        return word[:-1:]

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        """Creates an instance of the SpecialWordFinder class"""
        super().__init__(path)

    def random(self):
        clean_words = [word[:-1:] for word in self.words if not word.startswith('\\') and not word.startswith('#')]
        return choice(clean_words)