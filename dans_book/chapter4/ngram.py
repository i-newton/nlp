# -*- coding: UTF-8 -*-

import sys

import nltk
from nltk.util import ngrams

def main(argv):
    file = argv[0]
    with open(file, encoding="windows-1251") as txt_file:
        raw = txt_file.read()
        tokens = nltk.word_tokenize(raw)
        idx_split = int(0.7*len(tokens))
        train,test = tokens[:idx_split], tokens[idx_split:]
        text = nltk.Text(train)
        trigram_model = ngrams(text, 3)


if __name__ == "__main__":
    main(["data/war_peace.txt"])
