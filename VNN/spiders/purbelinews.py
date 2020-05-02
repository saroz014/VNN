# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class PurbelinewsSpider(scrapy.Spider):
    name = "purbelinews"
    # start_urls = ["http://purbelinews.com/%e0%a4%aa%e0%a4%b0%e0%a5%8d%e0%a4%af%e0%a4%9f%e0%a4%a8"]
    start_urls = ["http://purbelinews.com/पर्यटन"]

    def parse(self, response):
        unicode_response = response.body_as_unicode()
        html_response = Selector(text=unicode_response)
        title = html_response.css('article header h2.entry-title a::text').getall()
        image = html_response.css('article div.entry-thumbnail a img::attr(data-src)').getall()
        url = html_response.css('article header h2.entry-title a::attr(href)').getall()
        for item in zip(title, image, url):
            yield {'title': item[0],
                   'image': item[1],
                   'url': item[2]}

        if 'page' in response.url.split('/'):
            next_page = self.start_urls[0] + '/page/' + str(int(response.url.split('/')[-1]) + 1)
        else:
            next_page = self.start_urls[0] + '/page/2'
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
