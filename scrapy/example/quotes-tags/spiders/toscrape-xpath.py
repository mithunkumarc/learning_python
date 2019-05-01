# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        #print('**',len(response.xpath('//span[@class="tag-item"]/a[@class="tag"]')))
        for block in response.xpath('//span[@class="tag-item"][1]'):
            yield {"selector":str(block.xpath('./a[@class="tag"]/text()').extract_first())}

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        print('**',next_page_url,'**')
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


        # for quote in response.xpath('//div[@class="quote"]'):
        #     yield {
        #         'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
        #         'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
        #         'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
        #     }
        #
        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # print('**',next_page_url,'**')
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

