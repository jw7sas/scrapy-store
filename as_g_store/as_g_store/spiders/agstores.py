import scrapy

class AsGeekStore(scrapy.Spider):
    name = 'as_stores'
    start_urls = [
        'https://jw7sas.github.io/tshops/index.html'
    ]
    custom_settings = {
        'FEED_URI': 'stores.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY': True
    }

    def parse(self,response):
        store_links = response.xpath('//div[contains(@class, "content-panel")]//a[contains(@class, "panel-block")]/@href').getall()

        for link in store_links:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//div[contains(@class, "asgeek-container")]//h1[contains(@class, "asgeek-title")]/text()').get()

        yield {
            'title': title,
            'url': link
        }