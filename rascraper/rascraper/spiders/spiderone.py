import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'

    artist = input(f'Artist Name:')
    filter = input(f'filter on Country? (y/n):')

    if filter == 'y':
        country = input(f'Country:')
        start_urls = [
            f'https://ra.co/dj/{artist}/past-events?country={country}'
        ]

    elif filter == 'n':
        start_urls = [
            f'https://ra.co/dj/{artist}/past-events'
        ]

    HEADERS = {
        'accept': '/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
        'authorization': 'df67dacc9c704696b908a618dd4f59be',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': 'https://ra.co',
        'referer': 'https://ra.co/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
    }


    def parse(self, response):

        for post in response.css(''):

            date = post.css('.Text-sc-1t0gn2o-0.jmZufm::text').get()
            event = post.css('.Text-sc-1t0gn2o-0.Link__StyledLink-k7o46r-0.dXQVFW::text').get()
            location = post.css('.Text-sc-1t0gn2o-0.Link__StyledLink-k7o46r-0.echVma::text').get()
            venue = post.css('.Text-sc-1t0gn2o-0.Link__StyledLink-k7o46r-0.dxNiKF::text').get()
            acts = post.css('.Text-sc-1t0gn2o-0.bYvpkM::text').get()

            item = {}
            item['Date'] = date
            item['Event'] = event
            item['Location'] = location
            item['Venue'] = venue
            item['Acts'] = acts

            yield item