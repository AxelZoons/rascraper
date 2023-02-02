from rascraper.spiders.spiderone import PostsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import rascraper
# import os



def main():

    # 'settings' - relative path to setting.py file from 'main.py'
    # os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'rascraper/settings')

    process = CrawlerProcess(get_project_settings())
    process.crawl(PostsSpider)
    process.start()
    input('Pres ENTER to exit')

if __name__ == '__main__':
    main()