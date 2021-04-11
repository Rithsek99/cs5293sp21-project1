import spacy
import glob

nlp = spacy.load('en_core_web_sm')
#redact date method
def redactDate(doc):
        nlp_doc = nlp(doc)
        re = []
        num = 0
        #print(nlp_doc)
        for ent in nlp_doc:
            if ent.ent_type_ == "DATE":
                re.append("(REDACTED)")
                num +=1
            else:
                re.append(ent.text)
        return ' '.join(re),num

def test_date():

    text = "I will graduate on May 13th"
    re, n = redactDate(text)
    assert True
    assert n == 2
    assert re == "I will graduate on (REDACTED) (REDACTED)"
