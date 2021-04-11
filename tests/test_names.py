import spacy
import glob
import argparse
from spacy.matcher import Matcher
#from PyDictionary import PyDictionary
#dic=PyDictionary()
nlp = spacy.load('en_core_web_sm')
nlp.pipe_names
ner = nlp.get_pipe('ner')

#redact name method
def redactName(doc):
        nlp_doc = nlp(doc)
        re = []
        num = 0
        #print(nlp_doc)                
        for ent in nlp_doc:
            if ent.ent_type_ == "PERSON":
                re.append("(REDACTED)")
                num +=1
            else:
                re.append(ent.text)
        return ' '.join(re), num
def test_name():

    text = "John and Rithsek Ngme."
    result, num = redactName(text)
    print(result)
    assert True
    #test number of redact name
    assert num == 3
    assert result =="(REDACTED) and (REDACTED) (REDACTED) ."

