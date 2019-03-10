#The NLTK corpus is a massive dump of all kinds of natural language data sets.
#These files are plain text files for the most part, some are XML and some are other formats, but they are all accessible by you manually, or via the module and Python.

#Depending on your installation, your nltk_data directory might be hiding in a multitude of locations.
#To figure out where it is, head to your Python directory, where the NLTK module is.
#If you do not know where that is, use the following code:

import nltk
print(nltk.__file__)

#Run that, and the output will be the location of the NLTK module's __init__.py.

#NLTK module has a few nice methods for handling the corpus, so you may find it useful to use their methology.
#Here's an example of us opening the Gutenberg Bible, and reading the first few lines:

from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

# sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])

