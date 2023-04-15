import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrappy.items import LuckyItem


class myScrapy(scrapy.Spider):
    name = "lucky"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/']

    def parse(self, response, **kwargs):
        sel = scrapy.Selector(response)
        item = LuckyItem()
        item['title'] = sel.xpath('//title/text()').extract_first()
        yield item


# 获取settings.py文件中的配置
settings = get_project_settings()
# settings = Settings()
# settings.setmodule("lucky.settings", priority="project")

process = CrawlerProcess(settings)

process.crawl(myScrapy)
process.start()
