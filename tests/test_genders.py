import spacy
import glob
import argparse
from spacy.matcher import Matcher
#from PyDictionary import PyDictionary
#dic=PyDictionary()
nlp = spacy.load('en_core_web_sm')

def redactGender(doc):
        nlp_doc = nlp(doc)
        re = []
        num = 0
        gender = ["male","female","mother", "father","brother", "sister", "grandmother", "grandfather","uncle", "aunt","gentleman", "lady","king","queen","monk","nun","husband","wife","sir","madam","newphew","niece","actor","actress","son","daughter"]
        temp = doc.split()
        for item in temp:
            if item.lower() in gender:
                doc = doc.replace(item, "(REDACTED)")
                num +=1
        return doc, num


def test_gender():
    text = "The King is the husband of Sara."
    re, n = redactGender(text)
    assert True
    assert n == 2
    assert re == "The (REDACTED) is the (REDACTED) of Sara."
