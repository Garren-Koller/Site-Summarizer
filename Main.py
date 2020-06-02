from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.html import HtmlParser
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.utils import get_stop_words


def summarize():
    print("Enter a URL:")
    website = str(input())
    print("Enter Sentence amount:")
    sentence_count = int(input())

    LANGUAGE = "english"
    SENTENCES_COUNT = sentence_count

    url = website
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)


summarize()
