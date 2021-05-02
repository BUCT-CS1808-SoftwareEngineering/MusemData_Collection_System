# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MuseumPipeline:

    fp = None
    #重写父类的方法：开始的时候打印一次
    def open_spider(self,spider):
        print('开始爬虫......')
        self.fp = open('./museum.txt','w',encoding='utf-8')

    #专门处理item类型的对象
    #该方法用于接收爬虫文件提交过来的item对象
    #该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        name = item['museumName']
        f_name = item['museumForName']
        intro = item['introduction']
        time = item['time']
        location = item['location']
        cate = item['category']
        price = item['price']

        self.fp.write(name + '\n' + f_name + '\n' + intro + '\n'
        + time + '\n' + location + '\n' + cate + '\n' + price + '\n\n\n'
        )

        return item #传递给下一个即将被执行的管道类
    
    #重写父类的结束爬虫的方法
    def close_spider(self,spider):
        print('结束爬虫！')
        self.fp.close()


    # def process_item(self, item, spider):
    #     print(item['location'])
    #     return item
