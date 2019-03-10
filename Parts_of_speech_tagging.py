
# One of the more powerful aspects of the NLTK module is the Part of Speech tagging that it can do for you.
# This means labeling words in a sentence as nouns, adjectives, verbs...etc. Even more impressive,
# it also labels by tense, and more. Here's a list of the tags, what they mean, and some examples:-

'''
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent\'s
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
'''

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#PunktSentenceTokenizer is capable of unsupervised machine learning, so you can actually train it on any body of text that you use.

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

#Next, we can train the Punkt tokenizer like:

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

#Then we can actually tokenize, using:
tokenized = custom_sent_tokenizer.tokenize(sample_text)

#Now we can finish up this part of speech tagging script by creating a function that will run through and tag all of the parts of speech per sentence like so:

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))


process_content()

#The output should be a list of tuples, where the first element in the tuple is the word, and the second is the part of speech tag.