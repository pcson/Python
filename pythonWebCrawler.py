
__author__ = 'Paul Son'
__email__ = 'pcson@ischool.berkeley.edu'
__python_version = '2.7.3'
__can_anonymously_use_as_example = False

import urllib
from bs4 import BeautifulSoup
import re
import string
import webbrowser

# Does BFS on pages and gathers the words on each page. 
# This function is highly influenced by the BFS psuedocode found on wikipedia
# --http://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
def find_url():
    url = 'http://courses.ischool.berkeley.edu/i206/f13/a6-sandbox/index.html'
    stuffWeNeedToProcess = [] # List of pages we know about but haven't processed
    stuffWeHaveSeen = [] # Everything we know about. Either have or will process in the future
    # The first URL seed we plant to get the crawler started
    stuffWeNeedToProcess.append(url)
    stuffWeHaveSeen.append(url)
    # Counts how many links we FIND but not necessarily follow
    linksWeFound = 0

    # Loops so long as the list of items to process is not empty
    while len(stuffWeNeedToProcess) > 0:
        # Pops out a url that we need to 
        url_WeAreProcessing = stuffWeNeedToProcess.pop(0)
        # For everything links from url_WeAreProcessing
        linksFound = getAllLinks(url_WeAreProcessing) # Returns a list for each cycle of the loop
        for link in linksFound:
            # Adds to counter for each page we FIND but not follow
            linksWeFound +=1
            # If the link isn't something we've seen
            if link not in stuffWeHaveSeen:
                # Add
                link = str(link)
                stuffWeHaveSeen.append(link)
                stuffWeNeedToProcess.append(link)

    return 'BFS',stuffWeHaveSeen, len(stuffWeHaveSeen), linksWeFound, len(stuffWeHaveSeen)-1

# Prints out the crawlers results
def url_find_print():
    # Function call. Gets corresponding information from find_url()
    searchType, stuffWeHaveSeen, pagesCrawled, linksFound, linksFollowed = find_url()
    # Output
    print 'The Search Type:', searchType
    print "List of Pages Found: "
    # Declares range for loop
    rangeLength = range(0,len(stuffWeHaveSeen))
    for i in rangeLength:
        print stuffWeHaveSeen[i]
    print 'Total Number of Pages Crawled: ', pagesCrawled
    print "Total Number of Links Found: ", linksFound
    print "Total Number of Links Followed: ", linksFollowed

# Finds all the urls in the page
# Used in find_url()
def getAllLinks(url):                  
    root = urllib.urlopen(url).read()
    root_soup = BeautifulSoup(root)
    list_url = []
    mainUrl = 'http://courses.ischool.berkeley.edu/i206/f13/a6-sandbox/'
    #dictionary_url = {}

    for link in root_soup.find_all('a'):
        endUrl = link.get('href')
        whole = mainUrl+endUrl
        list_url.append(whole)
        #dictionary_url[link]
    return list_url


def main():
    url_find_print()

if __name__ == '__main__':
    main()

