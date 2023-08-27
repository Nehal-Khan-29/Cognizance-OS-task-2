import scrapy

class nehalspider(scrapy.Spider):
    name = "nehal_ghost"
    start_urls = ["https://www.amazon.in/s?k=watches+for+men&sprefix=watches%2Caps%2C309&ref=nb_sb_ss_ts-doa-p_1_7/"]
    
    def parse(self, response):
        for products in response.css('div.a-section.a-spacing-small.puis-padding-left-micro.puis-padding-right-micro'):
            yield {
                'Name': products.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get(),
                'Brand': products.css('span::text').get(),
                'Discount Price': products.css('span.a-price-whole::text').get(),
                'Discount Percent': products.xpath('.//span[@class="a-letter-space"]/following-sibling::span/text()').get(),
                'Rating':products.css('span.a-icon-alt::text').get(),
                'Views':products.css('span.a-size-base.s-underline-text::text').get(),
                'Get it by':products.css('span.a-color-base.a-text-bold::text').get()
            }