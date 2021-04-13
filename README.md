# cs5293sp21-project1

### Name: Rithsek Ngem

## How to run the program:
pipenv run python redactor.py --input '*.txt' --names "" --genders "" --dates "" --phone "" --concept 'kids'--output 'files/' --stats

## How to run test:
pipenv run pytest or pipenv run python -m pyest

## function:
* redactName(doc): take doc as argument and use nlp to find entity type as person to redact. the function return doc with names being redacted 
* redactDate(doc): function use nlp to find type date and redact it. the function return doc with dates being redacted
* redactPronoun(doc): this function redact pronound that identify gender, for example, he, she, and return doc with pronound being redacted
* redactGender(doc): this function redact gender in doc, (I defind gender list that contain words identify gender, i.e. king, monk, mother..), this function return doc with gender being redacted. 
* redactPhone(doc): this function redact phone number. In order to find phone number, I use matcher to find partern of phone number. The function return doc with phone number being redacted.
* redactConcept(doc, concept): this fuction take doc and concept as argument. ### I define concept by using synonym library to find the words that has the same meaning of concept and redact the sentence that contain this word. 
* main(inputfile, concept): this main fuction take inputfile directory and concept as argument, it calls the rest of functions to exectute the program. 

## Assumption
Assumption I made while writing code

* use spacy, nlp and nltk to define type of PERSON, DATE to look for name and date in document, 
* since spacy doesnt have fuction to recognize gender, I create list that contain word which identify gender and use to redact gender in document.
* I use re/matcher to create partern to look for phone number. 
* There is many different way to define the concept. I chose the synonym of word of the concept and iterate every word of synonym(concept) in the document and redact the sentence that contain that word. 
## Bug occure while writing code and expect to occure when executing
* spacy funtion to detect Date is not working properly. It detects some Data format but not the whole Date format. 
* since I only use one word as the concept, my program will not be able to detect if a phrase of concept is given. 
* argparse: I could not make it run as project example of execution, but How to run program above work just fine. 
## Test 
