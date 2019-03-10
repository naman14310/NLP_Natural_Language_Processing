'''
The goal with text classification can be pretty broad.
Maybe we're trying to classify text as about politics or the military.
Maybe we're trying to classify it by the gender of the author who wrote it.
A fairly popular text classification task is to identify a body of text as either spam or not spam, for things like email filters.
In our case, we're going to try to create a sentiment analysis algorithm.

To do this, we're going to start by trying to use the movie reviews database that is part of the NLTK corpus.
From there we'll try to use words as "features" which are a part of either a positive or negative movie review.
The NLTK corpus movie_reviews data set has the reviews, and they are labeled already as positive or negative.
This means we can train and test with this data.
'''

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

#Basically, in plain English, the above code is translated to: In each category (we have pos or neg),
#take all of the file IDs (each review has its own ID),
#then store the word_tokenized version (a list of words) for the file ID,
#followed by the positive or negative label in one big list.

#above code is one liner of this code:
#documents = []
#for category in movie_reviews.categories():
       #for fileid in movie_reviews.fileids(category):
            #documents.append(list(movie_reviews.words(fileid) , category)


random.shuffle(documents)

#Next, we use random to shuffle our documents. This is because we're going to be training and testing.
#If we left them in order, chances are we'd train on all of the negatives, some positives,
#and then test only against positives. We don't want that, so we shuffle the data.

print(documents)
#Then, just so you can see the data you are working with, we print out documents[1], which is a big list,
#where the first element is a list the words, and the 2nd element is the "pos" or "neg" label.



all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words.most_common(15))
#we can have a massive list of typical words. From here, we can perform a frequency distribution, to then find out the most common words.
#As you will see, the most popular "words" are actually things like punctuation, "the," "a" and so on, but quickly we get to legitimate words.

#You can also find out how many occurences a word has by doing:
print(all_words["stupid"])