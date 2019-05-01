#### spiders used to crawl data from site

        you can use css path or xpath        
        any number of spiders can be created, each spider to crawl each site/page/series of pages 


#### below example uses xpath

        parse method contains logic to extract data
        
        

#### example 1 :  crawling single page

    # inside parse method : parse method belongs to subclass of spider class 
    
    eg : class ToScrapeSpiderXPath(scrapy.Spider):


    def parse(self, response):
        # select all node with tag-item in doc(use //), from this node read text(use .) dot indication from current node
        # selecting all tags with tag-item
        for block in response.xpath('//span[@class="tag-item"]'):  
            # (data : tag names)going to file json/xml  
            yield {"selector": block.xpath('./a[@class="tag"]/text()').extract_first()}  
        yield scrapy.Request()  # important to return
        
        
        Note : to read selector path : below line will help you which path you are selecting
        
                yield {"selector":str(block.xpath('./a[@class="tag"]/text()'))}  


#### use yield function to extract to json/xml file

              parse method must have return statement which contains scrapy.Request(), 

              scrapy.Request() object can be empty or keep continue crawl to next page





#### example 2 : crawling multile page

    def parse(self, response):
        
        for block in response.xpath('//span[@class="tag-item"]'):
            yield {"selector":block.xpath('./a[@class="tag"]/text()').extract_first()}

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()		# eg : /page/2/

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))   # to the current url join /page/2/ .. so on


#### command to run :

      syntax : scrapy crawl <spider_name.py> -o <destination_file_name.json/xml>
      project name>scrapy crawl toscrape-xpath -o quotes.json

#### output : 

          sitename : http://quotes.toscrape.com/

          extracted data : 
          [
          {"selector": "love"},
          {"selector": "inspirational"},
          {"selector": "life"},
          {"selector": "humor"},
          {"selector": "books"},
          {"selector": "reading"},
          {"selector": "friendship"},
          {"selector": "friends"},
          {"selector": "truth"},
          {"selector": "simile"},
          {"selector": "love"},
          ... 
          ]

          ... : repeats same as number of pages, becase in each path tags have same data
