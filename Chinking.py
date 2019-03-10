#You may find that, after a lot of chunking, you have some words in your chunk you still do not want, but you have no idea how to get rid of them by chunking.
# ou may find that chinking is your solution.
#Chinking is a lot like chunking, it is basically a way for you to remove a chunk from a chunk.
#The chunk that you remove from your chunk is your chink.

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            chunked.draw()

    except Exception as e:
        print(str(e))

process_content()

# Chunk: {<.*>+} means chunk or all parts of speach.

#Now, the main difference here is:

# }<VB.?|IN|DT|TO>+{
# This means we're removing from the chink one or more verbs, prepositions, determiners, or the word 'to'.