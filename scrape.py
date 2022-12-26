from bs4 import BeautifulSoup
import requests
import csv


## this will return a responce object 
## to get the source code from that responce object we can add on .text to the end
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

## opening a csv file 
## we want to write to this file. That's why we use 'w'
csv_file = open('cms_scrape.csv', 'w')

## setting another variable and using a 'writer' method of the 'csv' module
csv_writer = csv.writer(csv_file)

## we want to write the headers of the csv file 
## creating a list and passing the headers
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):

    ## text from the first article and the first headline and the first aachor tag .a
    ## then .text to get the text out of this anchor tag
    ## .h2 is the parent tag of the anchor tag .a
    headline = article.h2.a.text
    print(headline)

    ## SUMMARY
    ## we are serching for a div with a specific class 
    ## within this div we want to parce out the first paragraph .p
    ## within this paragraph we want the text of this paragraph
    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    ## we want to find an iframe with a specific class
    ## if you want to get an attribute of a tag, you can access it like a dictionary  ['src']

    ## vid_src = article.find('iframe', class_ ='youtube-player')['src']

    ## now we want to extract the id of the video. For that we need to split the link on '/'
    ## after spliting we can find our id under idex 4
    ## vid_id = vid_src.split('/')[4]
    
    ## now to get the id we need to split what we have on a question mark
    ## vid_id = vid_id.split('?')[0]

    ## now we want to use this id to access the youtube video
    ##  yt_link = f'https://youtube.come/watch?v={vid_id}'
    ##  print(yt_link)

    try:
        vid_src = article.find('iframe', class_ ='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.come/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    
    print(yt_link)
    
    print()

    ## writing a data to the csv file with each itteration of our for loop
    csv_writer.writerow([headline, summary, yt_link])

## close the file at the end of the script
csv_file.close()