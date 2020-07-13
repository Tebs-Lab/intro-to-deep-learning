#USAGE : python testing.py goldenbridge

#TODO : *From the command line itself - specify the o/p folder path, no. of photos etc
#	*Understand a bit what flickr is doing
#	*Put code on Github






import flickr
import urllib, urlparse
import os
import sys

#Take user input
print "--- Press <Enter> to stop entering the tags --- \n"
tag=[]
i=0
while 1:
    i+=1
    input_tag=raw_input('Enter tag %d : '%i )
    if input_tag=='':
        break;

    tag.append(input_tag)

if not tag:
    print "No tags entered, aborting!"
    exit(0)

images_count=input('Enter the total number of images you want to download : ')

#downloading image data
f = flickr.photos_search(tags=tag, tag_mode='all', per_page=images_count)
urllist = [] #store a list of what was downloaded

#downloading images
for k in f:
    url = k.getURL(size='Small 320', urlType='source')
    urllist.append(url) 
    image = urllib.URLopener()
    image.retrieve(url, os.path.basename(urlparse.urlparse(url).path)) 
    print 'downloading:', url
