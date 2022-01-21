"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:

    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder.from_file("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    
    def __init__(self, words):
        self.words = [word.rstrip('\n') for word in words]
        print("{num} words read".format(num = len(self.words)))


    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f: 
            words = f.readlines()
        return cls(words)
    
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):

    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder.from_file("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def __init__(self, words):
        WordFinder.__init__(self, words)
        
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f: 
            words = [line.rstrip() for line in f]
            words = [line for line in words if line and not line.startswith('#')]
        return cls(words)
    
    def random(self):
        return WordFinder.random(self)