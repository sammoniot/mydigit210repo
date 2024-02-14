import os

import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
# nlp = spacy.cli.download("en_core_web_sm")

nlp = spacy.load('en_core_web_sm')
claude = open('sam-claude.txt', 'r', encoding='utf8')
words = claude.read()
wordstrings = str(words)
print(wordstrings)
# start playing with spaCy and nlp:
aiWords = nlp(wordstrings)
for token in aiWords:
    # if token.pos_ == "VERB":
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)

workingDir = os.getcwd()
print("current working directory: " + workingDir)
CollPath = os.path.join(workingDir, 'textCollection')
def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        # print(readFile)
        stringFile = str(readFile)
        lengthFile = len(readFile)
        print(lengthFile)

