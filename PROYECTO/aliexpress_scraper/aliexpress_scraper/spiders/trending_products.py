import scrapy

class TrendingProductsSpider(scrapy.Spider):
    name = "trending_products"
    allowed_domains = ["aliexpress.com"]
    start_urls = [
        "https://www.aliexpress.com/wholesale?catId=0&SearchText=trending"
    ]

    def parse(self, response):
        products = response.css(".list-item")
        for product in products:
            yield {
                "name": product.css(".item-title::text").get(),
                "price": product.css(".price-current::text").get(),
                "link": product.css("a::attr(href)").get(),
            }
