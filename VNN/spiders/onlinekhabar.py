# -*- coding: utf-8 -*-
import scrapy


class OnlinekhabarSpider(scrapy.Spider):
    name = "onlinekhabar"
    start_urls = ["https://www.onlinekhabar.com/content/nepalbeauty"]

    def parse(self, response):
        title = response.css('div.item__wrap a::text').getall()
        image = response.css('div.item.hasImg a img::attr(src)').getall()
        url = response.css('div.item.hasImg a::attr(href)').getall()
        for item in zip(title, image, url):
            yield {'title': item[0],
                   'image': item[1],
                   'url': item[2]}

        next_page = response.css('div.paginate-links a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
