# VNN

Visit Nepal News, a scrapy project to scrape tourism/travel news of Nepal from different news sites.

Note: This project only scrapes news links not the news itself.

## Requirements

`pip3 install -r requirements.txt`

## Usage

```
scrapy crawl <spider_name> -o <file_name>.json
```
Example command to scrape tourism/travel news of onlinekhabar.com:
```
scrapy crawl onlinekhabar -o onlinekhabar.json
```
Output will be title, image and url of the news.