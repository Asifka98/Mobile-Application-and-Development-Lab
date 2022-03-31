from cgitb import text
import nltk

text
txt = " Raju and Rani are friends"\
    " Maya is Raju friend"\
    " Raju is going to marry Maya"\
    " Their common friend is Rani"

print("Text  : \n", txt)

words = nltk.word_tokenize(txt)
print("Words in text : \n", words)

grammer = r" NP : {}"
regexparser = nltk.RegexpParser(grammer)
tagged = nltk.pos_tag(words)
chunked = regexparser.parse(tagged)

print(chunked)
