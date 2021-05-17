import scrapy
from museum.items import exhibitionItem 
import re
# scrapy crawl exhibition1
# 故宫


class Exhibition1Spider(scrapy.Spider):
    name = 'exhibition1'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.dpm.org.cn/searchs/exhibition/category_id/301/pagesize/6.html?0.13021943427510996&tpl_file=shows_temporary2_2&exhibition_status=0&showstype=301&order=1']
    # start_urls =['https://www.dpm.org.cn/searchs/exhibition/category_id/301/pagesize/6/tpl_file/shows_temporary2_2/exhibition_status/0/showstype/301/order/1/p/1.html']

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'Secure; Secure; Secure; Secure; Secure; UM_distinctid=178deb1a5f29b4-0781b55b2eb662-3f356b-1fa400-178deb1a5f3ba0; PHPSESSID=e75e287d2be2f78b0f068d7c5117a1d3; saw_terminal=default; saw_seasonal=%E9%BB%98%E8%AE%A4; cn_1263553186_dplus=%7B%22distinct_id%22%3A%20%22178deb1a5f29b4-0781b55b2eb662-3f356b-1fa400-178deb1a5f3ba0%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201619006799%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201619006799%7D; cn_1278672694_dplus=%7B%22distinct_id%22%3A%20%22178deb1a5f29b4-0781b55b2eb662-3f356b-1fa400-178deb1a5f3ba0%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201619339759%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201619339759%2C%22initial_view_time%22%3A%20%221619145149%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referrer_domain%22%3A%20%22%24direct%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D; CNZZDATA1261553859=82839869-1618639799-https%253A%252F%252Fcn.bing.com%252F%7C1619345517; cn_1261553859_dplus=%7B%22distinct_id%22%3A%20%22178deb1a5f29b4-0781b55b2eb662-3f356b-1fa400-178deb1a5f3ba0%22%2C%22%24_sessionid%22%3A%201%2C%22%24_sessionTime%22%3A%201619350532%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201619350532%2C%22initial_view_time%22%3A%20%221618639799%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22initial_referrer_domain%22%3A%20%22cn.bing.com%22%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D; acw_tc=65c86a0c16193629093602963efdd1658032fc54e79bfa8519e5c6fd9d6333',
        'Host': 'www.dpm.org.cn',
        'Referer': 'https://www.dpm.org.cn/shows.html',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    num = 0

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)

    def parse_detail(self, response):
        item = response.meta["item"]
        print(item["exhibName"])
        print(item['exhibImg'])
        # exhib_time = response.xpath('/html/body/div/div[3]/div[1]/div/div[3]/div/p[1]/span[1]/em/text()').extract_first()
        # exhib_location = response.xpath('/html/body/div/div[3]/div[1]/div/div[3]/div/p[1]/span[2]/em/text()').extract_first()
        exhib_intro = '暂无'
        if response.xpath('//*[@id="_exName"]/div[2]//text()').extract():
            exhib_intro = response.xpath('//*[@id="_exName"]/div[2]//text()').extract()
            exhib_intro = ''.join(exhib_intro)
        # s = ''
        # for i in range(len(exhib_intro)):
        #     exhib_intro[i] = str(exhib_intro[i])
        #     s += re.sub(r'\\u3000','',exhib_intro[i])     
        # print(exhib_time)
        # print(exhib_location)
        item["exhibIntro"] = exhib_intro
        print(item["exhibIntro"])
        self.num += 1
        yield item

    # https://www.dpm.org.cn/searchs/exhibition/category_id/301/pagesize/6/tpl_file/shows_temporary2_2/exhibition_status/0/showstype/301/order/1/p/2.html

    def parse(self, response):
        # m = response.xpath('//*[@id="temporary2_list"]').extract()
        # print(m)
        # //*[@id="temporary2_list"]/div[1]
        # div_list = response.xpath('//*[@id="temporary2_list"]/div[1]/div')
        div_list = response.xpath('//*[@class="list clearfix"]/div')
        for div in div_list:
            item = exhibitionItem()
            # //*[@id="temporary2_list"]/div[1]/div[1]/div[2]/div/div[1]/a[1]
            exhib_name = div.xpath('./div[2]/div/div[1]/a[1]/text()').extract_first()
            # if exhib_name != None:
                # print(exhib_name)
            item["museumID"] = 1
            item["exhibName"] = exhib_name
            # print(item["exhibName"])
            img = 'https://www.dpm.org.cn' + div.xpath('./div[1]/a/img/@src').extract_first()
            item['exhibImg'] = img
            # print(item['exhibImg'])
            detail_url = div.xpath('./div[1]/a/@href').extract_first()
            if detail_url[0] == '/':
                detail_url = 'https://www.dpm.org.cn' + detail_url
            # print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})


