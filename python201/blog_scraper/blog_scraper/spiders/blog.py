from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from ..items import BlogScraperItem # import the class we created earlie

class MyBlogSpider(BaseSpider): # subclass BaseSpider
    name = 'mouse'
    start_urls = ['http://blog.pythonlibrary.org']

    # This is the most important
    # Takes the responses from the URL and parses them
    def parse(self, response):
        selector = Selector(response)
        # xpath used for navigating XML documents
        blog_titles = selector.xpath("//h1[@class='entry-title']") # found with inspect element
        selections = []

        for data in blog_titles:
            selection = BlogScraperItem()
            selection['title'] = data.xpath("a/text()").extract()
            selection['link'] = data.xpath("a/@href").extract()
            selections.append(selection)

        return selections
