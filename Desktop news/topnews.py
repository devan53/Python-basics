import requests
import csv
import xml.etree.ElementTree as ET

# url of news rss feed
url = "https://www.hindustantimes.com/rss/india/rssfeed.xml"

def loadRSS():
    '''
    utility function to load RSS feed 
    '''
    # create HTTP request response object
    resp = requests.get(url)
    # return response content
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)

def parseXML(xmlfile):
    '''
    utility function to parse XML format rss feed
    '''
    # create element tree root object
    root = (ET.parse(xmlfile)).getroot()
    # create empty list for news items
    newsitems = []
    
    # iterate news items
    for item in root.findall('./channel/item'):
        news = {}
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text
        newsitems.append(news)
 
    # return news items list
    return newsitems

def savetoCSV(newsitems,filename):
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media'] 
  
    # writing to csv file 
    with open(filename, 'w+') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(newsitems)

def topStories():
    # load rss feed
    loadRSS()
    # parse XML
    newsitems = parseXML('topnewsfeed.xml')
    return newsitems
    
##
##def main():
##    # load rss feed
##    loadRSS()
##    # parse XML
##    newsitems = parseXML('topnewsfeed.xml')
##    # store news items in a csv file 
##    savetoCSV(newsitems, 'topnews.csv') 


##if __name__ == "__main__": 
##  
##    # calling main function 
##    main() 
