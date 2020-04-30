import scrapy


class SetopatiSpider(scrapy.Spider):
    name = "setopati"
    start_urls = ["https://www.setopati.com/ghumphir"]

    def parse(self, response):
        feature_title = response.css('div.big-feature figure a::attr(title)').get()
        feature_image = response.css('div.big-feature figure a figure img::attr(src)').get()
        feature_url = response.css('div.big-feature figure a::attr(href)').get()
        yield {'title': feature_title,
               'image': feature_image,
               'url': feature_url}
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_next)

    def parse_next(self, response):
        title = response.css('div.news-cat-list div.items a::attr(title)').getall()
        image = response.css('div.news-cat-list div.items a figure img::attr(src)').getall()
        url = response.css('div.news-cat-list div.items a::attr(href)').getall()
        for item in zip(title, image, url):
            yield {'title': item[0],
                   'image': item[1],
                   'url': item[2]}

        try:
            next_page = response.css('div.pagination a.nextpostslink::attr(href)').getall()[1]
        except IndexError:
            next_page = response.css('div.pagination a.nextpostslink::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_next)
