# -*- coding: utf-8 -*-
import urllib2

import re

import os

from os.path import basename

from urlparse import urlsplit

from urlparse import urlparse

from posixpath import basename,dirname


class DataController:

    def __init__(self):
        pass

    

    def downloadForagidos(self):
        url='http://www2.defesasocial.rn.gov.br/foragidos/index.html' ## give the url here
        url2img='http://www2.defesasocial.rn.gov.br/foragidos/'

        parse_object=urlparse(url)

        dirname=basename(parse_object.path)
        
        if not os.path.exists('images'):
            
            os.mkdir("images")
            
            os.mkdir("images/"+dirname)

            os.chdir("images/"+dirname)

            urlcontent=urllib2.urlopen(url).read()
            
            imgurls=re.findall('img .*?src="(.*?)"',urlcontent)
            
            for imgurl in imgurls:

                print(url2img+imgurl)
                
                imgurl = process_url(imgurl)
                imgurl = imgurl.decode('utf-8')
                imgurl = imgurl.encode('latin_1')
                print(url2img+imgurl)
                
                imgdata=urllib2.urlopen(url2img + imgurl).read()
                
                filname=basename(urlsplit(imgurl)[2])
                print(filname)
                
                output=open(filname,'wb')
                
                output.write(imgdata)

                
                
                output.close()

    def update(self):
        pass

def process_url(raw_url):
	
    if ' ' not in raw_url[-1]:
        
        raw_url=raw_url.replace(' ','%20')
        
        return raw_url

    elif ' ' in raw_url[-1]:
        
        raw_url=raw_url[:-1]

        raw_url=raw_url.replace(' ','%20')
        
        return raw_url