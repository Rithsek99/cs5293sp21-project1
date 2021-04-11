import spacy
import glob
import nltk
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
nlp.pipe_names
ner = nlp.get_pipe('ner')

#redact name method
def redactName(doc):
    nlp_doc = nlp(doc)
    re = []
    #print(nlp_doc)                
    for ent in nlp_doc:
        if ent.ent_type_ == "PERSON":
            re.append("(REDACTED)")
        else:
            re.append(ent.text)
    return ' '.join(re)

#redact date method
def redactDate(doc):
    nlp_doc = nlp(doc)
    re = []
    #print(nlp_doc)
    for ent in nlp_doc:
        if ent.ent_type_ == "DATE":
            re.append("(REDACTED)")
        else:
            re.append(ent.text)
    return ' '.join(re)
#redact Prounoun
def redactPronoun(doc):
    nlp_doc = nlp(doc)
    re = []
    pro =["he","she","him","her","himself","herself","his","hers"]
    #print(nlp_doc)
    for ent in nlp_doc:
        if ent.text.lower() in pro:
            re.append("(REDACTED)")
        else:
            re.append(ent.text)
    return ' '.join(re)
#redact NNP
def redactNNP (doc):
    nlp_doc = nlp(doc)
    re = []
   # print(nlp_doc)
    for ent in nlp_doc:
        if ent.ent_type_ =="NNP":
            re.append("(REDACTED)")
        else:
            re.append(ent.text)
    return ' '.join(re)
#redact Gener
def redactGender(doc):
    nlp_doc = nlp(doc)
    re = []
    gender = ["male","female","mother", "father","brother", "sister", "grandmother", "grandfather","uncle", "aunt","gentleman", "lady","king","queen","monk","nun","husband","wife","sir","madam","newphew","niece","actor","actress","son","daughter"]
    temp = doc.split()
    for item in temp:
        if item.lower() in gender:
            doc = doc.replace(item, "(REDACTED)")
    return doc
#redact phone number

def redactPhone(doc):
    nlp_doc = nlp(doc)
    re = []
    matcher = Matcher(nlp.vocab)
    pattern = [{"ORTH": "("}, {"SHAPE": "ddd"}, {"ORTH": ")"}, {"SHAPE": "ddd"},
                       {"ORTH": "-", "OP": "?"}, {"SHAPE": "dddd"}]
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
    return temp
def main():
    #print(redactName(doc))
    dire = glob.glob("inputFile/*.txt")
    #print(dire)
    for f in dire:
        temp_f = open(f,"r")
        #redact phone
        temp = redactPhone(temp_f.read())
        # redact date
        temp = redactDate(temp)
        # redact name
        temp = redactName(temp)
        #redact gender
        temp = redactGender(temp)
        #redact Prounoun
        temp = redactPronoun(temp)
        name = f.split(".")
        result = open(name[0]+".redacted","w")
        result.write(temp)

if __name__ == '__main__':
    main()

