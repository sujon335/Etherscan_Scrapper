import scrapy
import json
import time

class EtherScanSpider(scrapy.Spider):
     name = "code_spider"
     with open('contents.json') as f:
         data = json.load(f)
     start_urls=[]    
     for i in range(0,len(data),1):
         version=data[i]["version"]
         if(version is None):
             continue
          ## add the below condition to crawl version specific solidity codes    
          #if( version !="v0.4.26" and version !="v0.4.25" and version !="v0.4.24" and version !="v0.4.23" and version !="v0.4.22"):
         address=data[i]["address"]
         address='https://etherscan.io'+address
             #print(address)
         start_urls.append(address)


     def parse(self, response):
         X_SELECTOR = '.hidden-su-custom'
         address=response.css(X_SELECTOR)
         Y_SELECTOR=  '#mainaddress ::text'
         SET_SELECTOR = '.panel-sourcecode'
         for etherset in response.css(SET_SELECTOR):
             NAME_SELECTOR = '.js-sourcecopyarea ::text'
             yield {
                     'file': address.css(Y_SELECTOR).extract_first(),
                     'code': etherset.css(NAME_SELECTOR).extract_first(),
                   }
    
