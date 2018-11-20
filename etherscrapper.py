import scrapy
import time

class EtherScanSpider(scrapy.Spider):
     name = "EtherScan_Spider"
     start_urls = ['https://etherscan.io/contractsVerified']

     def parse(self, response):
         SET_SELECTOR = 'tr'
         for etherset in response.css(SET_SELECTOR):
             NAME_SELECTOR = 'a ::attr(href)'
             VERSION_SELECTOR = 'td[3]/text()'
             yield {
                     'address': etherset.css(NAME_SELECTOR).extract_first(),
                     'version': etherset.xpath(VERSION_SELECTOR).extract_first(),
                   }
             
         NEXT_PAGE_SELECTOR = '.btn-default.logout ::attr(href)'
         next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
         next_page ='https://etherscan.io'+ next_page
         print(next_page)
         if next_page:
             yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
