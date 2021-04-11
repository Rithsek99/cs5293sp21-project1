import spacy
import glob
import argparse
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')

def redactPhone(doc):
        nlp_doc = nlp(doc)
        re = []
        num_redact = 0
        matcher = Matcher(nlp.vocab)
        pattern = [{"ORTH": "("}, {"SHAPE": "ddd"}, {"ORTH": ")"}, {"SHAPE": "ddd"}, {"ORTH": "-", "OP": "?"}, {"SHAPE": "dddd"}]
        matcher.add("PHONE_NUMBER", [pattern])
        #print(nlp_doc)
        matches = matcher(nlp_doc)
        for match_id, start, end in matches:
            span = nlp_doc[start:end]
            re.append(span.text) 
        temp = doc
        for item in re:
            if item in temp:
                temp = temp.replace(item, "(REDACTED)")
                num_redact += 1 
        return temp, num_redact


def test_phone():
    text = "Call me at (123) 456 7849 or (123) 456 7489!"
    re,n = redactPhone(text)
    assert True
    assert n == 2
    assert re == "Call me at (REDACTED) or (REDACTED)!"
