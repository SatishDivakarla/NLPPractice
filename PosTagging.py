__author__ = 'divakarla'

'''
CC	Coordinating conjunction
CD	Cardinal number
DT	Determiner
EX	Existential there
FW	Foreign word
IN	Preposition or subordinating conjunction
JJ	Adjective
JJR	Adjective, comparative
JJS	Adjective, superlative
LS	List item marker
MD	Modal
NN	Noun, singular or mass
NNS	Noun, plural
NNP	Proper noun, singular
NNPS	Proper noun, plural
PDT	Predeterminer
POS	Possessive ending
PRP	Personal pronoun
PRP$	Possessive pronoun
RB	Adverb
RBR	Adverb, comparative
RBS	Adverb, superlative
RP	Particle
SYM	Symbol
TO	to
UH	Interjection
VB	Verb, base form
VBD	Verb, past tense
VBG	Verb, gerund or present participle
VBN	Verb, past participle
VBP	Verb, non-3rd person singular present
VBZ	Verb, 3rd person singular present
WDT	Wh-determiner
WP	Wh-pronoun
WP$	Possessive wh-pronoun
WRB	Wh-adverb
'''

import nltk
import re

#example_array = ['The incredibly intimidating NLP scares people away who are sissies.']
example_array = ["This isn't a greater love story"]

def processLanguage():
    try:
        for item in example_array:
            #Tokenizing the string
            tokenized = nltk.word_tokenize(item)

            # Parts of Speech Tagging the tokens wot
            tagged =  nltk.pos_tag(tokenized)
            print tagged

            #Chunking
            #chunkGram = r"""Chunk:{<RB\w?>*<VB\w?>*<NNP>}"""
            chunkGram = r"""Chunk:{<RB\w?>*<JJ\w?>}"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            print chunked
            chunked.draw()

    except Exception, e:
        print str(e)
def getAdjectives():
    try:
        for item in example_array:
            tokenized = nltk.word_tokenize(item)
            tagged =  nltk.pos_tag(tokenized)
            print tagged
            for tagIndex in tagged:
                if (tagIndex[1] =='JJ' or tagIndex[1] =='JJR' or tagIndex[1] =='JJS' or tagIndex[1] =='RB' or tagIndex[1] =='RBR' or tagIndex[1] =='RBS'):
                    print tagIndex[0]

    except Exception, e:
        print str(e)


#processLanguage()
getAdjectives()