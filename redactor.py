import spacy
import glob
import nltk
import argparse
from spacy.matcher import Matcher
from PyDictionary import PyDictionary
dic=PyDictionary()
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
#redact Prounoun
def redactPronoun(doc):
    nlp_doc = nlp(doc)
    re = []
    num = 0
    pro =["he","she","him","her","himself","herself","his","hers"]
    #print(nlp_doc)
    for ent in nlp_doc:
        if ent.text.lower() in pro:
            re.append("(REDACTED)")
            num +=1
        else:
            re.append(ent.text)
    return ' '.join(re), num
#redact Gener
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
#redact phone number

def redactPhone(doc):
    nlp_doc = nlp(doc)
    re = []
    num_redact = 0
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
            num_redact += 1 
    return temp, num_redact
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
def main():
    #print(redactName(doc))
    dire = glob.glob("inputFile/*.txt")
    #print(dire)
    for f in dire:
        temp_f = open(f,"r")
        #redact phone
        temp,phone_redact = redactPhone(temp_f.read())
        #print("this file"+ f.split(".")[0]+"has "+str(phone_redact)+" redacted")
        # redact date
        temp,date_redact = redactDate(temp)
        # redact name
        temp,name_redact = redactName(temp)
        #redact gender
        temp,gender_redact = redactGender(temp)
        #redact Prounoun
        temp,pro_redact = redactPronoun(temp)
        #redact concept
        temp,conc_redact = redactConcept(temp,"crime")
        name = f.split(".")
        result = open(name[0]+".redacted","w")
        result.write(temp)
        result.write("type "+  "---" + " num of redact\n")
        result.write("Name" + " --- " + str(name_redact)+"\n")
        result.write("Phone" + " --- "+ str(phone_redact)+"\n")
        result.write("Date" + " --- "+ str(date_redact)+"\n")
        result.write("Gender" + " --- "+ str(gender_redact+pro_redact)+"\n")
        result.write("Concept"+" --- "+ str(conc_redact)+"\n")
        print(name[0] + "  type "+"---"+ " num of redact")
        print("Name" + " --- " + str(name_redact))
        print("Phone" + " --- "+ str(phone_redact))
        print("Date" + " --- "+ str(date_redact))
        print("Gender" + " --- "+ str(gender_redact+pro_redact))
        print("Concept"+" --- "+ str(conc_redact))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True,"--names", type = str, required = False )# "--dates")            #  "--phones", "--genders","--concept", type=str, required=True,
          #  "--output",type=str, required= True,
         #   "--state",type=stderr)
    args = parser.parse_args()
    print(args.input)
    #main()

