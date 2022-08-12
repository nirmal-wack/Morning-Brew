from email.mime import image
from gnewsclient import gnewsclient
import tkinter as tk
import nltk
from pymongo import MongoClient
from newspaper import Article

# mongodb client 
admin = MongoClient("mongodb+srv://:@cluster0.txsxmsq.mongodb.net/?retryWrites=true&w")

#mongo calling database
db = admin.get_database('india')
#mongo calling table
records = db.sports
# c = records.count_documents({})

# creating client to fetch news
client = gnewsclient.NewsClient(language='English',
                              location='india',
                              topic='Kabbadi',
                              max_results=5)

#getting news                              
items = client.get_news()

arr_news = []
arr_collect = []
i = 0
# from all news(items) collect news's title and summary

for ns in items :

  # title of news
  temp = ns['title']
  #url to fetch news with hwlp of Article library
  url = str(ns['link'])
  
  article = Article(url)
  article.download()
  article.parse()
  article.nlp()
  k = article.images
  print(k)
  img = '/Users/sandipshah/Desktop/ptec/index.js'

  new_record = { 'title' : temp , 'summary' : str(article.summary) , 'img' : '/Users/sandipshah/Desktop/ptec/index.js' }
  records.insert_one(new_record)

  i += 1
 
