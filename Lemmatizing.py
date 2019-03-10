#A very similar operation to stemming is called lemmatizing.
#The major difference between these is, as you saw earlier, stemming can often create non-existent words, whereas lemmas are actual words.

#Some times you will wind up with a very similar word, but sometimes, you will wind up with a completely different word.

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))

#The only major thing to note is that lemmatize takes a part of speech parameter, "pos."
#If not supplied, the default is "noun."
