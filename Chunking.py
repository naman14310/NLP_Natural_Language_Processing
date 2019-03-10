#One of the main goals of chunking is to group into what are known as "noun phrases."
#These are phrases of one or more words that contain a noun, maybe some descriptive words, maybe a verb, and maybe something like an adverb.
#The idea is to group nouns with the words that are in relation to them.

#In order to chunk, we combine the part of speech tags with regular expressions.
#Mainly from regular expressions, we are going to utilize the following:
# + = match 1 or more
# ? = match 0 or 1 repetitions.
# * = match 0 or MORE repetitions
# . = Any character except a new line

#The part of speech tags are denoted with the "<" and ">" and we can also place regular expressions within the tags themselves,
#so account for things like "all nouns" (<N.*>)

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            for subtree in chunked.subtrees():
                print(subtree)

            chunked.draw()

            # What is happening here is our "chunked" variable is an NLTK tree.
            # Each "chunk" and "non chunk" is a "subtree" of the tree.
            # We can reference these by doing something like chunked.subtrees.
            # We can then iterate through these subtrees like so:

            #Next, we might be only interested in getting just the chunks, ignoring the rest.
            #We can use the filter parameter in the chunked.subtrees() call.

            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print(subtree)

            #Keep in mind, this isn't "Chunk" as in the NLTK chunk attribute... this is "Chunk" literally because that's the label we gave it here: chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            #Had we said instead something like chunkGram = r"""Pythons: {<RB.?>*<VB.?>*<NNP>+<NN>?}""", then we would filter by the label of "Pythons."


    except Exception as e:
        print(str(e))

process_content()

#The main line here in question is:

#chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
#This line, broken down:

#<RB.?>* = "0 or more of any tense of adverb," followed by:
#<VB.?>* = "0 or more of any tense of verb," followed by:
#<NNP>+ = "One or more proper nouns," followed by
#<NN>? = "zero or one singular noun."



