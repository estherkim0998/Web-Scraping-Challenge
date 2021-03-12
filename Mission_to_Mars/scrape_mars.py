#!/usr/bin/env python
# coding: utf-8

# In[98]:


#import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from pprint import pprint
import pymongo
import requests
from webdriver_manager.chrome import ChromeDriverManager


# In[89]:


#executable_path

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[90]:


#visit the nasa mars site

url = ('https://mars.nasa.gov/news/')
browser.visit(url)
html= browser.html
soup = bs(html, 'html.parser')


# In[91]:


print(soup.prettify())


# In[70]:


# all titles and bodies
titles = soup.find_all('div', class_="content_title")
print(titles)
body = soup.find_all('div', class_="article_teaser_body")
print(body)


# In[71]:


# find first title and body
slides = soup.find_all('li', class_='slide')

title = slides[0].find('div', class_= 'content_title')
ttext = title.text.strip()
body = slides[0].find('div', class_= 'article_teaser_body')
btext = body.text.strip()

print(ttext)
print(btext)


# In[92]:


#quit browser
browser.quit


# In[94]:


#vist url
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[83]:


#get image 
images = soup.find_all('img', class_='headerimage fade-in')
print(images)


# In[86]:


#get just src
for image in images:
   pic = (image['src'])
print(pic)


# In[87]:


#get image url
featured_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{pic}'
print(featured_url)


# In[100]:


#Mars Fact
df = pd.read_html("https://space-facts.com/mars/")[0]
df.columns =["Description","Mars"]
df.set_index("Description", inplace=True)
df


# In[101]:


df.to_html()


# In[112]:


# Hemisphere
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[113]:


hemisphere_image_urls = []
# Fist get a list of all the hemisphere
links = browser.find_by_css("a.product-item h3")


for index in range(len(links)):
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[index].click()
    
    #Next is find the sample image anchor tag and extract the href
    sample_element = browser.links.find_by_text("Sample").first
    title = browser.find_by_css("h2.title").text
    link =sample_element["href"]
    hemisphere["title"] = title
    hemisphere["link"] = link
    
    hemisphere_image_urls.append(hemisphere)
    print("Retrieve url and link")
    browser.back()
    
print(hemisphere_image_urls)


# In[114]:


browser.quit


# In[ ]:




