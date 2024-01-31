import spacy
# Need line 8 the first time: Then comment it out after the first time you run it:
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')
claude = open('claudeaitestprompt.txt', 'r', encoding='utf8')
words = claude.read()
wordstrings = str(words)
print(wordstrings)
# start playing with spaCy and nlp:
aiWords = nlp(wordstrings)
for token in aiWords:
    # if token.pos_ == "VERB":
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)