import scrapy
from scrapy.utils.project import get_project_settings


class ArticlesSpider(scrapy.Spider):
    name = "articles"
    start_urls = [
        'https://www.heise.de/newsticker/archiv/?jahr=2017;woche=1',
    ]

    #  archiv_woche > ul:nth-child(5) > li:nth-child(1) > a
    #  archiv_woche > ul:nth-child(3) > li:nth-child(1) > a
    #  archiv_woche > ul:nth-child(3) > li:nth-child(1) > a

    # set up settings
    settings = get_project_settings()
    settings.overrides['ITEM_PIPELINES'] = {'__main__.MyPipeline': 1}


    def parse(self, response):
        x = 0
        for daysPerWeek in response.css('#archiv_woche'):
            for articlesPerDay in daysPerWeek.css('ul '):
                for article in articlesPerDay.css('li'):
                    yield {
                        'creationDate': daysPerWeek.css('h4::text').extract()[x],
                        'link': article.css('a::attr(href)').extract_first(),
                        'article': article.css('a::text').extract_first(),
                    }
                x += 1
        next_page = response.css(
            '#archiv_woche > p > a.archiv_woche_navigation_next::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
