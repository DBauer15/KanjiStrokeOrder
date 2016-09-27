# -*- coding: utf-8 -*-

import aqt
from anki.hooks import addHook
from aqt.utils import showInfo
import urllib2
import urllib
from bs4 import BeautifulSoup
from aqt.qt import *
import re


def cleanhtml(raw_html):
  cleanr =re.compile('<.*?>')
  cleantext = re.sub(cleanr,'', raw_html)
  return cleantext

def mungeQA(html, type, fields, model, data, col):
    try:
        raw = cleanhtml(html)

        if (type == 'q' and not len(raw) > 1):
            url = 'http://www.sp.cis.iwate-u.ac.jp/icampus/u/akanji.jsp?k='
            url += urllib.quote_plus(raw.encode('utf-8'))

            source = urllib2.urlopen(url).read()
            soup = BeautifulSoup(source, "html.parser")
            imgs = soup.findAll("img")
            filename = imgs[2]["src"].split("/")[-1]
            html+="<br/><br/><span style='align:center'><img src='http://www.sp.cis.iwate-u.ac.jp/icampus/u/sod/"+filename+"' width='500px'></span>"
            #showInfo("Munged: %s" % filename)
    except:
        print("Couldn't fetch stroke graph")

    return html


addHook("mungeQA", mungeQA)
