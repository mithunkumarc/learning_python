
####  trending searches : 


          import scrapy
          class ToScrapeSpiderXPath(scrapy.Spider):
              name = 'toscrape-xpath'
              start_urls = [
                  'https://in.bookmyshow.com/bengaluru',
              ]

              def parse(self, response):

                  for block in response.xpath('//div[@class="widget-card"]'):
                       yield {"movie title":block.xpath('./a/div/h4/text()').extract_first()}

                  yield scrapy.Request() # important to return request


              command to run :  scrapy crawl toscrape-xpath -o bookmyshow.json

              [
              {"movie title": "Avengers: Endgame"},
              {"movie title": "Majili"},
              {"movie title": "IPL Chennai Super Kings (Chennai)"},
              {"movie title": "Shazam!"},
              {"movie title": "99 (Kannada)"},
              {"movie title": "Kanchana 3"},
              {"movie title": "K.G.F. Chapter 2"},
              {"movie title": "Captain Marvel"}
              ]

---



#### movie image urls : 

              import scrapy
              class ToScrapeSpiderXPath(scrapy.Spider):
                  name = 'toscrape-xpath'
                  start_urls = [
                      'https://in.bookmyshow.com/bengaluru/movies',
                  ]

                  def parse(self, response):
                      count = 0
                      for block in response.xpath('//div[@class="card-img"]'):
                           count += 1
                           yield {f"image url {count}":block.xpath('./img/@data-src').extract_first()}

                      yield scrapy.Request() # important to return request


              command to run :  scrapy crawl toscrape-xpath -o bookmyshow.json

              output : 

              [
              {"image url 1": "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/avengers-end-game-et00090482-07-12-2018-06-50-21.jpg"},
              {"image url 2": "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/jersey-et00077973-19-06-2018-02-57-43.jpg"},
              {"image url 3": "//in.bmscdn.com/iedb/movies/images/mobile/thumbnail/xlarge/kavalu-daari-et00067133-13-12-2017-09-37-12.jpg"},
              ...


---

#### extracting privacy policy : 


            import scrapy
            class ToScrapeSpiderXPath(scrapy.Spider):
                name = 'toscrape-xpath'
                start_urls = [
                    'https://in.bookmyshow.com/bengaluru',
                ]

                def parse(self, response):

              # using absolute xpath : extracted from browser
                    # yield {'privacy policy' : response.xpath('/html/body/div[5]/footer/div[1]').extract_first()}
              # using xpath expression	
              yield {'privacy policy' : response.xpath('//div[@class="privacy-policy-footer"]/p').extract_first()}
                    yield scrapy.Request() # important to return request


            command to run :  scrapy crawl toscrape-xpath -o bookmyshow.json

            output : extracting policy, this policy contains links also

            from absolute path : 
            [
            {"privacy policy": "<div class=\"privacy-policy-footer\">\n        <h4>Privacy Note</h4>\n        <p>By using www.bookmyshow.com(our website), you are fully accepting the Privacy Policy available at <a href=\"/privacy\">https://bookmyshow.com/privacy</a> governing your access to Bookmyshow and provision of services by Bookmyshow to you. If you do not accept terms mentioned in the <a href=\"/privacy\">Privacy Policy</a>, you must not share any of your personal information and immediately exit Bookmyshow.</p>\n      </div>"}
            ]

            from xpath expression : 

            [
            {"privacy policy": "<p>By using www.bookmyshow.com(our website), you are fully accepting the Privacy Policy available at <a href=\"/privacy\">https://bookmyshow.com/privacy</a> governing your access to Bookmyshow and provision of services by Bookmyshow to you. If you do not accept terms mentioned in the <a href=\"/privacy\">Privacy Policy</a>, you must not share any of your personal information and immediately exit Bookmyshow.</p>"}
            ]

