import search
from bs4 import BeautifulSoup
import requests

#print(search.productInfo("B06W55K9N6","https://www.amazon.com/Western-Digital-Elements-Portable-External/dp/B06W55K9N6"))
def bsproduct(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url,headers = headers)
    # print(response.text)
    soup = BeautifulSoup(response.content,features = "lxml")
    title = soup.select("#productTitle")
    #price = soup.select("#priceblock_ourprice")[0].get_text()
    print(title)

bsproduct("https://www.amazon.com/Western-Digital-Elements-Portable-External/dp/B06W55K9N6")


