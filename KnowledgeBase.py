import time
import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import datetime
import sqlite3
import nltk

cj = CookieJar()
opener =  urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

conn = sqlite3.connect('knowledgeBase.db')
c = conn.cursor()

visitedLinks = []

# We need create DB to be executed only once.
#def createDB():
#    c.execute("CREATE TABLE knowledgeBase (unix REAL, datestamp TEXT, namedEntity TEXT, relatedWord TEXT)")

def processor(data):
    try:
        tokenized = nltk.word_tokenize(data)
        tagged = nltk.pos_tag(tokenized)
        namedEnt  = nltk.ne_chunk(tagged,binary=True)
        entities =  re.findall(r'NE\s(.*?)/',str(namedEnt))
        # print tagged
        # print entities
        # print entities

        # Descriptives
        descriptives =  re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'',str(tagged))


        if len(entities)>1:
            pass
        elif len(entities)==0:
            pass
        else:
            print '=================================='
            print 'Named :  ', entities[0]
            print 'Descriptions : '
            for eachDesc in descriptives:
                print eachDesc
                currenttime = time.time();
                datestamp =  datetime.datetime.fromtimestamp(currenttime).strftime('%Y-%m-%d %H:%M:%S')
                namedEntity = entities[0]
                relatedWord = eachDesc
                c.execute("INSERT INTO knowledgeBase(unix,datestamp,namedEntity,relatedWord)  VALUES (?,?,?,?)",
                    (currenttime,datestamp,namedEntity,relatedWord))
                conn.commit()

    except Exception, e:
        print 'failed in the first try of processor'
        print str(e)


def huffingtonRSSVisit():
    try:
        page = 'http://feeds.huffingtonpost.com/huffingtonpost/raw_feed'
        sourceCode =  opener.open(page).read()
        try:
            links  = re.findall(r'<link.*href=\"(.*?)\"',sourceCode)
            for link in links:
                if '.rdf' in link:
                    pass
                elif link in visitedLinks:
                    print 'link already visited'
                else:
                    visitedLinks.append(link)
                    print 'Visiting the link'
                    print '###################'
                    linkSource = opener.open(link).read()
                    linesOfInterest = re.findall(r'<p>(.*?)</p>',str(linkSource))
                    print 'Content:'
                    for eachLine in linesOfInterest:
                        if '<img width' in eachLine:
                            pass
                        elif '<a href' in eachLine:
                            pass
                        else:
                       #     print eachLine
                            processor(eachLine)

                    time.sleep(5)


        except Exception, e:
            print 'Failed main loop of huffingtonRSS'
            print str(e)

    except Exception, e:
        print 'Failed main loop of huffingtonRSS'
        print str(e)


while 1<2:
    currenttime = time.time();
    datestamp =  datetime.datetime.fromtimestamp(currenttime).strftime('%Y-%m-%d %H:%M:%S')
    huffingtonRSSVisit()
    time.sleep(900)
    print "sleeping"
    print datestamp