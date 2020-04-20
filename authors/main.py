import requests
import time
import yaml
import urllib.parse

from string import Template

from bs4 import BeautifulSoup

'''
https://stackoverflow.com/questions/22623798/google-search-with-python-requests-library

https://developers.google.com/custom-search/docs/xml_results#WebSearch_Request_Format
'''

HEADERS_GET = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}


def googleSearch_scrap(q):

    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r = s.get(url, headers=HEADERS_GET)

    soup = BeautifulSoup(r.text, "html.parser")
    output = []
    for searchWrapper in soup.find_all('h3', {'class':'r'}): #this line may change in future based on google's web page structure
        url = searchWrapper.find('a')["href"] 
        text = searchWrapper.find('a').text.strip()
        result = {'text': text, 'url': url}
        output.append(result)

    return output

def googleSearch(query):
    '''Oh hell just scrap it
    '''
    s = requests.Session()
    url = 'https://www.google.com/search?q=' + urllib.parse.quote(query) + '&ie=utf-8&oe=utf-8'
    r = s.get(url, headers=HEADERS_GET)
    soup = BeautifulSoup(r.text, "html.parser")
    for searchWrapper in soup.find_all('div', {'class', 'r'}):
        a1 = searchWrapper.find("a")
        print(a1.text)
        print("\t" + a1.attrs['href'])
    return 

def fn():
    f = "/home/jkern/src/authors/people.yml"
    people = None
    with open(f) as fd:
        people = yaml.load(fd, Loader=yaml.FullLoader)
    for person in people['people']:
        googleSearch(person['name'])
        time.sleep(0.25)


def sort_names():
    f = "/home/jkern/src/authors/people.yml"
    people = None
    with open(f) as fd:
        people = yaml.load(fd, Loader=yaml.FullLoader)
    whoswho = []
    for person in people['people']:
        whoswho.append(person["name"])
    for name in sorted(whoswho):
        print(name)


if __name__ == "__main__":
    sort_names()
