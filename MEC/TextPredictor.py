from word_predictor import WordPredictor
import nltk

wp = WordPredictor()
for corpus in nltk.corpus.gutenberg.fileids():
    wp.learn_from_text(nltk.corpus.gutenberg.raw(corpus))
print ("Ready")
while True:
    phrase = input()
    print (wp.predict(phrase).terms()[0:3])
