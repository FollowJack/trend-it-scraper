import scrapy


class ArticlesSpider(scrapy.Spider):
    name = "articles"
    start_urls = [
        'https://www.heise.de/newsticker/archiv/?jahr=2017;woche=1',
    ]

    #  archiv_woche > ul:nth-child(5) > li:nth-child(1) > a
    #  archiv_woche > ul:nth-child(3) > li:nth-child(1) > a
    #  archiv_woche > ul:nth-child(3) > li:nth-child(1) > a

    def parse(self, response):  # archiv_woche > ul:nth-child(3) > li:nth-child(2) > a
        for daysPerWeek in response.css('#archiv_woche'):
            for articlesPerDay in daysPerWeek.css('ul '):
                for article in articlesPerDay.css('li'):
                    yield {
                        'creationDate': daysPerWeek.css('h4::text').extract()[2],
                        'link': article.css('a::attr(href)').extract_first(),
                        'article': article.css('a::text').extract_first(),
                    }

                    # next_page = response.css('li.next a::attr("href")').extract_first()
                    # if next_page is not None:
                    #     next_page = response.urljoin(next_page)
                    #     yield scrapy.Request(next_page, callback=self.parse)
