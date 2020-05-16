from googlesearch import search
import requests
from lxml import html

def searchname(productq):
    query = 'inurl:amazon.com ' + productq
    links = search(query, tld='com', lang='en', num=1, start=0, stop=1)
    for link in links:
        urllen = link.split("dp/",1)
        if len(urllen) == 1:
            return { 'id':"404a99"}      
        return productInfo(urllen[1],link)

def productInfo(pid,link):
    print('data processing')
    amazon_url = link
    print(amazon_url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    page = requests.get(amazon_url,headers = headers,verify=True)
    page_response = page.text
    parser = html.fromstring(page_response)
    XPATH_AGGREGATE = '//span[@id="acrCustomerReviewText"]'
    #XPATH_AGGREGATE_RATING = '//table[@id="histogramTable"]//tr'
    XPATH_PRODUCT_NAME = '//h1//a[@data-hook="product-link"]//text()'
    XPATH_PRODUCT_PRICE  = '//span[@class="a-color-price arp-price"]/text()'
    #XPATH_TOTAL_REVIEWS= '//span[@data-hook="total-review-count"]/text()'
    
    raw_product_price = parser.xpath(XPATH_PRODUCT_PRICE)
    product_price = ''.join(raw_product_price).replace(',','')
    raw_product_name = parser.xpath(XPATH_PRODUCT_NAME)
    product_name = ''.join(raw_product_name).strip()
    print(product_name)
    data = {
                'id': pid,
				'name':product_name,
				'url':link,
				'price':product_price,
			}
    return data
