from googlesearch import search
from Naked.toolshed.shell import execute_js, muterun_js
import json

def searchname(productq):
    query = 'inurl:amazon.com ' + productq
    links = search(query, tld='com', lang='en', num=1, start=0, stop=1)
    for link in links:
        urllen = link.split("dp/",1)
        if len(urllen) == 1:
            return { 'id':"404a99"}      
        return productInfo(urllen[1],link)

def productInfo(pid,link):
    success = execute_js('scraper/product-data.js',link)
    if success :
        with open('scraper/data/prodata.json', 'r',encoding="utf8") as f:
            pdata = json.load(f)
        data = {
                'id': pid,
				'name':pdata['title'],
				'url':link,
				'price':pdata['price'],
			}
        return data
