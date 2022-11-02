import  scrapy

from demo.items import BookItem


class MySpider(scrapy.Spider):
    name = "mySpider"
    start_urls=['http://127.0.0.1:5000']
    # def start_requests(self):
    #     url='http://127.0.0.1:5000'
    #     yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response, **kwargs):
       try:
           data = response.body.decode()
           selector = scrapy.Selector(text=data)
           books = selector.xpath("//book")
           for book in  books:
               iter = BookItem()
               iter["title"] = book.xpath("./title/text()").extract_first()
               iter["author"] = book.xpath("./author/text()").extract_first()
               iter["publisher"] = book.xpath("./publisher/text()").extract_first()
               yield  iter
       except Exception as  err:
           print(err)