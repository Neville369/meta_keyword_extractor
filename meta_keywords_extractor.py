from bs4 import BeautifulSoup as bs
import requests as rq
import lxml
import re

# Read URLs from the text file 
with open('urls.txt','r') as file:
    urls = [line.strip().rstrip(',')
            for line in file
            if line.strip()]
    
# Function to get the keywords of a webpage 
def get_keywords(url):
    try:
        response = rq.get(url)
        response.raise_for_status()
        soup = bs(response.content,'lxml')
        meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
        keywords = meta_keywords['content'] if meta_keywords else ''
        return keywords
    except rq.RequestException as e:
        return
    
# Iterate over each url and print the meta_keywords 
for url in urls:
   if url:  # Check if URL is not empty
        keyword = get_keywords(url)
        print(f'keywords of {url}: {keyword}')








        