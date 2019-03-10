#WordNet is a lexical database for the English language, which was created by Princeton, and is part of the NLTK corpus.
#You can use WordNet alongside the NLTK module to find the meanings of words, synonyms, antonyms, and more.

from nltk.corpus import wordnet

#Then, we're going to use the term "program" to find synsets like so:
syns = wordnet.synsets("program")
for s in syns:
    print(s.name())

#Just the word:
print(syns[0].lemmas()[0].name())

#Definition of that first synset:
print(syns[0].definition())

#Examples of the word in use:
print(syns[0].examples())

#Next, how might we discern synonyms and antonyms to a word?
#The lemmas will be synonyms, and then you can use .antonyms to find the antonyms to the lemmas.

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#Next, we can also easily use WordNet to compare the similarity of two words and their tenses,
#by incorporating the Wu and Palmer method for semantic related-ness.

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))
#0.9090909090909091

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))
#0.6956521739130435

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))
#0.38095238095238093