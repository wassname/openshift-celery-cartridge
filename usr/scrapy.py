from scrapy.settings import CrawlerSettings
from scrapy.crawler import CrawlerProcess

spider_example_name = 'news_spider'

appname = 'openshift'

os.environ.setdefault('SCRAPER_SETTINGS_MODULE', '{0}.scraper.settings'.format(appname))
scrapy_settings_model = __import__(os.getenv('SCRAPER_SETTINGS_MODULE'), fromlist=[''])


settings = CrawlerSettings(scrapy_settings_model)
prs = CrawlerProcess(settings)
crawler = prs.create_crawler()
for name, spd in crawler.spiders._spiders.iteritems():
    if name == spider_example_name:
        spidercls = spd
crawler.crawl(spidercls(id=1))
prs.start()
