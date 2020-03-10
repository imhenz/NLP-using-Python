import re

import nltk
from matplotlib import rcParams
from spacy.lang.de import German
from spacy.lang.de.stop_words import STOP_WORDS
from wordcloud import *
import matplotlib.pyplot as plt

import re

import nltk
from matplotlib import rcParams
from spacy.lang.de import German
from spacy.lang.de.stop_words import STOP_WORDS
from wordcloud import *
import matplotlib.pyplot as plt


class NaturalLanguageProcessing:

    def __init__(self, filename):

        self._nlp = German()
        self._myfile = open(filename, encoding="utf8")
        self._text = self._nlp(
            re.sub(r'[^a-zA-Z_\s_\t]+', '', self._myfile.read().replace('\n', '').replace('\t', '').replace('  ', '')))

    def dataprocessing(self, ):
        token_list = []
        for token in self._text:
            token_list.append(token.text)
        tokens = [token.lower() for token in token_list if token is not '']
        return tokens

    def textanalizer(self, ):
        token_list = self.dataprocessing()
        tokens = []
        for word in token_list:
            wordcheck = self._nlp.vocab[word]
            if wordcheck.is_stop == False:
                tokens.append(word.replace(' ', ''))

        freq = nltk.FreqDist(tokens)
        freq.most_common(52)
        freq.plot(20, cumulative=False)

    def visualization(self, ):

        tokens = self.dataprocessing()
        stopwords = STOP_WORDS
        wd = WordCloud(stopwords=stopwords, background_color="black", max_words=50).generate(' '.join(tokens))
        rcParams['figure.figsize'] = 10, 20
        plt.imshow(wd, interpolation='bilinear')
        plt.axis("off")
        plt.show()
