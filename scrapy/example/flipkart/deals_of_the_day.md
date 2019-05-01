#### deals of the day :

              import scrapy
              class ToScrapeSpiderXPath(scrapy.Spider):
                  name = 'toscrape-xpath'
                  start_urls = [
                      'https://www.flipkart.com/',
                  ]

                  def parse(self, response):
                      count = 0
                      for block in response.xpath('//a[@class="K6IBc- required-tracking"]'):
                          count += 1
                          yield {
                                  'item_count' : count,
                                  'item_name' : block.xpath('./div[@class="iUmrbN"]/text()').extract_first(),
                                  'item_discount' : block.xpath('./div[@class="BXlZdc"]/text()').extract_first(),
                                  'item_category' : block.xpath('./div[@class="_3o3r66"]/text()').extract_first()
                                 }
                      yield scrapy.Request() # important to return request

output : 

              command to run : scrapy crawl toscrape-xpath -o flipkart.json


              [
              {"item_count": 1, "item_name": "Glue Guns", "item_discount": "Under \u20b9299", "item_category": "Best Selling"},
              {"item_count": 2, "item_name": "Nike & Asics", "item_discount": "Upto 45%+Extra 5% ", "item_category": "Walking, Running Shoes &  more"},
              {"item_count": 3, "item_name": "Catwalk, Bata & more ", "item_discount": "Under \u20b9899+Extra 5%", "item_category": "Grab a great pair now!"},
              {"item_count": 4, "item_name": "Bata, Newport & more", "item_discount": "Under \u20b9799+Extra 5%", "item_category": "Sneakers, Formal Shoes & more"},
              {"item_count": 5, "item_name": "Mobile Back Covers", "item_discount": "Just \u20b9149", "item_category": "For All Top Models"},
              {"item_count": 6, "item_name": "Trimmer, Straightener & more ", "item_discount": "From \u20b9649 ", "item_category": "By Philips"},
              {"item_count": 7, "item_name": "Safari, American Tourister...", "item_discount": "Flat 50% Off", "item_category": "Trolleys, Duffels & more"},
              {"item_count": 8, "item_name": "Skybags, American Tourister...", "item_discount": "Upto 80%+Extra5%Off", "item_category": "Backpacks, Trolleys, Wallets..."}
              ]
