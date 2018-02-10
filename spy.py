import scrapy

class ZomatoSpider(scrapy.Spider):
    name = 'spy'

    def start_requests(self):
        urls = [
            'https://www.reddit.com/r/gameofthrones//',
            'https://www.reddit.com/r/game/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        author = response.css('a.author.may-blank::text').extract()
        comments = response.css('.comments::text').extract()
       
        for item in zip(titles,votes,times,comments,author):
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'created_at' : item[2],
                'created_by' : item[4],
                'comments' : item[3],
            }
            yield scraped_info
