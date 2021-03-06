import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.tag import pos_tag, map_tag
import re

#Get postagger using the nltk tagger
def getPosTag(word):

    token = word_tokenize(word)
    tagged = nltk.pos_tag(token)
    simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tagged]
    return list(sum(simplifiedTags, ()))


#Get synonyms based on the wordnet corpus with universal postag and wup_simiarity score
def getSynonyms(word):
    #nltk.download('wordnet')
    temp = wn.synsets(word)
    if(temp):
        synonyms = []
        words = []
        for syn in temp:
            for l in syn.lemmas():
                if(l.name() not in words):
                    words.append(l.name())
                    synTemp = getPosTag(l.name())
                    synTemp[0] = re.sub('_', ' ', synTemp[0])
                    synTemp.append(temp[0].wup_similarity(syn))
                    synonyms.append(synTemp)
        return synonyms
    else:
        return "not found"


#Get definitions based on the wordnet corpus
def getDefinition(word):
    temp = wn.synsets(word)
    if(temp):
        return temp[0].definition()
    else:
        return "not found"


#Get examples based on the wordnet corpus
def getExamples(word):
    temp = wn.synsets(word)
    if(temp):
        return temp[0].examples()
    else:
        return "not found"


