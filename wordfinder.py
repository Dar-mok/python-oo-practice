from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, file):
        """Creates an instance of the WordFinder class"""
        self.words = self.parse(open(file))


    def random(self):
        """Return a random word from a list of words"""
        return choice(self.words)

    def parse(self, file):
        """Removes whitespace around each line  """
        return [line.strip() for line in file]


class SpecialWordFinder(WordFinder):

    def parse(self, file):
        """Goes through a list of words and removes any words/lines starting with a # symbol and removes line breaks"""

        return  [word for word in super().parse(file) if word and not word.startswith('#')]
