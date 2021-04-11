import spacy
import glob
import argparse
from spacy.matcher import Matcher
from PyDictionary import PyDictionary
dic=PyDictionary()
nlp = spacy.load('en_core_web_sm')

#redact concept
def redactConcept(doc,concept):
    nlp_doc = nlp(doc)
    num = 0
    sent = doc.split(".") # split doc into list of sentense
    word = dic.synonym(concept) # get the list of synonym of concpet
    for i in range(len(sent)):
        for w in word:
            if w in sent[i]:
                sent[i] = "(REDACTED)"
                num += 1
    return ' '.join(sent),num


def test_concept():
    text = "there cybercrime in 2020 was the highest. Hope we can reduce it now."
    re, n = redactConcept(text,"crime")
    assert True
    assert n == 1
    assert re == "(REDACTED)  Hope we can reduce it now "
