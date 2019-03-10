# it removes ing or any other such forms from the words.
# for eg: 'ride' and 'riding' have same meaning so stemming process removes -ing from the word 'riding'.
#The idea of stemming is a sort of normalizing method. Many variations of words carry the same meaning, other than when tense is involved.
#The reason why we stem is to shorten the lookup, and normalize sentences.

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

#One of the most popular stemming algorithms is the Porter stemmer, which has been around since 1979.

ps = PorterStemmer()

example_words = ["python" , "pythoner" , "pythoning" , "pythoned"]

for w in example_words:
    print(ps.stem(w))

new_text = "it is very important to be pythonly while you are pythoning with python . All pythoners have pythoned poorlt atleast once ."

for w in word_tokenize(new_text):
    print(ps.stem(w))