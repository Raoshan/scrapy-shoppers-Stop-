import scrapy
from shoppersstop.items import ShoppersstopItem
from scrapy.linkextractors import LinkExtractor
class ShopperSpider(scrapy.Spider):
    name = 'shopper'    
    allowed_domains = ['www.shoppersstop.com']
    start_urls = ['https://www.shoppersstop.com/search/?text=jumpsuits']
   
    def parse(self, response):
        item = ShoppersstopItem()
        self.log('I just visited: '+response.url)
        for prod in response.css('div.li-inner'):
            name = prod.css('div.pro-name::text').get()             
            item['name'] = name
            link = prod.css('div.pro-info a::attr(href)').get()
            url = 'https://www.shoppersstop.com'+link
            print(url)
            item['url'] = url
            brand = prod.css('div.Brand-name::text').get()
            print(brand)
            item['brand'] = brand
            try:
                p = prod.css("li::text").extract()
                price = p[2].strip()
                print(price)
                item['price']  = price               
            except:
                rs = prod.css("div.price_div::text").extract()
                price = rs[2].strip()
                print(price)
                item['price'] = price
            imageUrl1 = prod.css('div.styleImagesMain').xpath('a[1]').css('img::attr(data-src)').get()
            print(imageUrl1)
            item['imageUrl1'] = imageUrl1
            imageUrl2 = prod.css('div.styleImagesMain').xpath('a[2]').css('img::attr(data-src)').get()
            print(imageUrl2)
            item['imageUrl2'] = imageUrl2
            
            yield item
        
     

        # next_page = response.css('link[id="preUrl"]').attrib['href']
        next_page = response.css('a.next').attrib['href']
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

      
      
