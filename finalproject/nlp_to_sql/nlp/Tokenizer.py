from nltk.tokenize.stanford import StanfordTokenizer
import os

class Tokenizer(object):
    """
    Tokenize sentence
    """
    def __init__(self, jar_path):
        self.tokenizer = StanfordTokenizer(jar_path)


    def tokenize(self, sentence):
        java_path = "D:/Software/Java/jdk-18.0.1.1/bin/java.exe"
        os.environ['JAVAHOME'] = java_path
        return self.tokenizer.tokenize(sentence)


    def __call__(self, sentence):
        return self.tokenize(sentence)
