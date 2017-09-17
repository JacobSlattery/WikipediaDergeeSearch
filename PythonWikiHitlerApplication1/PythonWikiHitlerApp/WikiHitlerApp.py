import requests
from bs4 import BeautifulSoup
import urllib.parse
import threading

hitlerLink = '/wiki/Adolf_Hitler'
wikiLink = '/wiki/'



#Gets all the links on the page body, and deletes the ref list, then returns a list of the links
def getWikiPageLinks(webpageURL):
    linkList = []
    page = requests.get(webpageURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('body')
    for div in soup.find_all('div', {'class':'reflist columns references-column-width'}): 
        div.decompose()
    for link in body.find_all('a', href=True):
        hrefLink = link.get('href')
        if hrefLink.startswith(wikiLink):
            fullLink = urllib.parse.urljoin('https://en.wikipedia.org', hrefLink)
            linkList.append(fullLink)
    return list(set(linkList))

#Testing around with grequesets
"""def goThroughEachLinkInList(linkList):
    levelTwoList = []
    for link in sorted(linkList, key=str.lower):
        fullLink = urllib.parse.urljoin('https://en.wikipedia.org', link)
        pageLinks = getWikiPageLinks(fullLink)
        levelTwoList.append(pageLinks)
    
    rs = (grequests.get(url) for url in levelTwoList)

    print(grequests.map(rs))"""

#Gets each link inside the list, turns them into urls, sorts them, prints each to screen, and sifts through their links for hitler
#Program stops if hitler is found
def goThroughEachLinkInList(linkList):
    levelTwoList = []
    for link in sorted(linkList, key=str.lower):
        pageLinks = getWikiPageLinks(link)
        levelTwoList.append(pageLinks)
        print(link)
        if isHitlerInList(pageLinks):
            return levelTwoList
    return levelTwoList

#Simply checks if hitler is in the list
def isHitlerInList(linkList):
    for link in linkList:
        if hitlerLink in link:
            return True
    return False

#Runs the programs needed to search for and find hitler.
#Calls getWikiPageLinks, isHitlerInList, and goThroughEachLinkInList
def findHitler():
    location = input('Please enter URL: ')
    print('Checking First Level...')
    myList = getWikiPageLinks(location)
    if isHitlerInList(myList):
        print('Site Directly Links To Hitler!')
        return
    print('Checking Second Level...')
    #newList = Pool(processes=4).map(goThroughEachLinkInList, myList)
    #newList = ThreadPool(2).imap(goThroughEachLinkInList, myList) This is throwing an error
    newList = goThroughEachLinkInList(myList) #This works but very slow
    """threads = [threading.Thread(target=goThroughEachLinkInList, args=(url,)) for url in myList]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()"""
    if isHitlerInList(threads):
        print('Site Directly Links To Hitler!')
        return
    else:
        print('Hitler Not Found')

findHitler()