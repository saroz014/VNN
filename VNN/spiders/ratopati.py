# -*- coding: utf-8 -*-
import scrapy


class RatopatiSpider(scrapy.Spider):
    name = 'ratopati'
    start_urls = ['http://ratopati.com/category/tourism']

    def parse(self, response):
        title = response.css('div.ot-articles-material-blog-list div.item div.item-content span a::text').getall()
        image = response.css('div.ot-articles-material-blog-list div.item div.item-header a img::attr(src)').getall()
        url = response.css('div.ot-articles-material-blog-list div.item div.item-content span a::attr(href)').getall()
        for item in zip(title, image, url):
            yield {'title': item[0],
                   'image': item[1],
                   'url': 'http://ratopati.com' + item[2]}

        next_page = response.css('div.ot-main-panel-pager a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
