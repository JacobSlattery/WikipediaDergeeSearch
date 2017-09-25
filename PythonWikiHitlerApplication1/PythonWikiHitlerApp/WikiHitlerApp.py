import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

hitlerLink = 'https://en.wikipedia.org/wiki/Adolf_Hitler'


#Gets all the links on the page body, and deletes the ref list, then returns a list of the links
def getWikiPageLinks(webpageURL):
    if not webpageURL:
        return False
    linkList = []
    page = requests.get(webpageURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('body')
    for div in soup.find_all('div', {'class':'reflist columns references-column-width'}): 
        div.decompose()
    for link in body.find_all('a', href=True):
        hrefLink = link.get('href')
        if hrefLink.startswith('/wiki/'):
            fullLink = urllib.parse.urljoin('https://en.wikipedia.org', hrefLink)
            linkList.append(fullLink)
            masterList.append(fullLink)
    return list(set(linkList))

#Gets each link inside the list, turns them into urls, sorts them, prints each to screen, and sifts through their links for hitler
#Program stops if hitler is found
def goThroughEachLinkInList(linkList):
    if not linkList:
        return False
    nextLevelList = []
    sortedList = sorted(list(set(linkList)), key=str.lower)
    print('There are ' + str(len(sortedList)) + ' links to search')
    count = 0
    for link in sortedList:
        count += 1
        print(str(count) + '. ' + link)
        pageLinks = getWikiPageLinks(link)
        nextLevelList.append(pageLinks)
        if isHitlerInList(pageLinks):
            return nextLevelList
    return nextLevelList

#Simply checks if hitler is in the list
def isHitlerInList(linkList):
    for link in linkList:
        if hitlerLink in link:
            #writeNewDirectLinkInFile(link)
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
    if isHitlerInList(goThroughEachLinkInList(list(set(masterList)))):
        print('Hitler Was Found!')
        return
    print('Checking Third Level...')
    if isHitlerInList(goThroughEachLinkInList(list(set(masterList)))):
        print('Hitler Was Found!')
        return
    else:
        print('Hitler not found')


findHitler()