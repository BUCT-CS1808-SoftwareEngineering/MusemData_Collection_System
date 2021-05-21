# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
from time import sleep

# class MuseumSpiderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.

#         # Should return None or raise an exception.
#         return None

#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.

#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i

#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.

#         # Should return either None or an iterable of Request or item objects.
#         pass

#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.

#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r

#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)


class MuseumDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
    #拦截响应对象进行篡改
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # 通过url指定request
        # 通过request指定response
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        if request.url in spider.new_urls:
            #针对定位到的篡改
            #实例化新的响应对象
            #基于selenium
            bro = spider.bro
            bro.get(request.url)
            bro.refresh()
            sleep(5)
            page_text = bro.page_source
            new_response = HtmlResponse(url = request.url,body = page_text,encoding = 'utf-8',request = request)

            return new_response

        elif request.url in spider.deep_urls:
            #针对定位到的篡改
            #实例化新的响应对象
            #基于selenium
            brom = spider.brom
            brom.get(request.url)
            sleep(5)
            page_text = brom.page_source
            deep_response = HtmlResponse(url = request.url,body = page_text,encoding = 'utf-8',request = request)

            return deep_response
        elif request.url in spider.js1_urls:
            #针对定位到的篡改
            #实例化新的响应对象
            #基于selenium
            bro = spider.bro
            bro.get(request.url)
            bro.refresh()
            # bro.refresh()
            sleep(5)
            for i in range(3):
                bro.find_element_by_css_selector("div.load-more").click()
            sleep(5)
            page_text = bro.page_source
            js_response = HtmlResponse(url = request.url,body = page_text,encoding = 'utf-8',request = request)

            return js_response
        elif request.url in spider.js2_urls:
            #针对定位到的篡改
            #实例化新的响应对象
            #基于selenium
            bro = spider.bro
            bro.get(request.url)
            bro.refresh()
            # bro.refresh()
            # sleep(5)
            for i in range(30):
                bro.find_element_by_css_selector(".layui-flow-more > a:nth-child(1)").click()
                sleep(3)
            # sleep(5)
            page_text = bro.page_source
            js_response = HtmlResponse(url = request.url,body = page_text,encoding = 'utf-8',request = request)

            return js_response
        elif request.url in spider.js3_urls:
            #针对定位到的篡改
            #实例化新的响应对象
            #基于selenium
            bro = spider.bro
            bro.get(request.url)
            bro.refresh()
            # bro.refresh()
            # sleep(5)
            # for i in range(5):
            bro.find_element_by_css_selector("body > div > div.ql-main > div > div.list-tab > div > div.ql-fl > div > ul > li:nth-child(4)").click()
            # body > div > div.ql-main > div > div.list-tab > div > div.ql-fl > div > ul > li.active
                # sleep(3)
            sleep(5)
            page_text = bro.page_source
            js_response = HtmlResponse(url = request.url,body = page_text,encoding = 'utf-8',request = request)

            return js_response
        else:
            return response
        # return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
