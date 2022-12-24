from bs4 import BeautifulSoup
import requests

## this will return a responce object 
## to get the source code from that responce object we can add on .text to the end
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

#print(article.prettify())

## text from the first article and the first headline and the first aachor tag .a
## then .text to get the text out of this anchor tag
## .h2 is the parent tag of the anchor tag .a
# headline = article.h2.a.text
# print(headline)

## SUMMARY
## we are serching for a div with a specific class 
## within this div we want to parce out the first paragraph .p
## within this paragraph we want the text of this paragraph
# summary = article.find('div', class_='entry-content').p.text
# print(summary)

## we want to find an iframe with a specific class
vid_src = article.find('iframe', class_ ='youtube-player')['src']
print(vid_src)

## if you want to get an attribute of a tag, you can access it like a dictionary  ['src']

