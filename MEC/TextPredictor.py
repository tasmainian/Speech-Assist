from word_predictor import WordPredictor
import nltk


wp = WordPredictor()
for corpus in nltk.corpus.gutenberg.fileids():
    wp.learn_from_text(nltk.corpus.gutenberg.raw(corpus))
    
def PredictNext(phrase):
    #return [('The',0.123),('Me',0.213123),('Hi', 0.1232)]
    return wp.predict(phrase).terms()[0:3]
