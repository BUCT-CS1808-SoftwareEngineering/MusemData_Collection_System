# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from pymysql.converters import escape_string


class MuseumPipeline:

    conn = None
    cursor = None
    def open_spider(self,spider):
        #连接数据库
        self.conn = pymysql.Connect(host='149.129.54.32',user = 'root',port = 3306,password = '',db = 'cs1808test',charset = 'utf8')
    def process_item(self,item,spider):
        #创建cursor对象
        self.cursor = self.conn.cursor()
        #错误判断
        try:
            #通过excute用sql语句操作数据库
            print(spider.name[0:10])
            if spider.name[0:10] == "collection":
                self.cursor.execute('insert into `collection info table`(muse_ID,col_Name,col_Intro,col_Photo) values("%d","%s","%s","%s")'%(item["museumID"],item["collectionName"],item["collectionIntroduction"],item["collectionImage"]))
                self.conn.commit()
            elif spider.name[0:10] == "exhibition":
                self.cursor.execute('insert into `exhibition info table`(muse_ID,exhib_Name,exhib_Content,exhib_Pic) values("%d","%s","%s","%s")'%(item["museumID"],item["exhibName"],item["exhibIntro"],item["exhibImg"]))
                self.conn.commit()
            elif spider.name[0:9] == "education":
                self.cursor.execute('insert into `education act table`(muse_ID,act_Name,act_Content,act_Pic) values("%d","%s","%s","%s")'%(item["museumID"],item["eduName"],item["eduContent"],item["eduImg"]))
                self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

class MuseumTestPipeline:

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


    def process_item(self, item, spider):
        print(item['location'])
        return item
#管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
class mysqlPipeLine:
    conn = None
    cursor = None
    def open_spider(self,spider):
        #连接数据库
        self.conn = pymysql.Connect(host='149.129.54.32',user = 'root',port = 3306,password = '',db = 'cs1808test',charset = 'utf8')
    def process_item(self,item,spider):
        #创建cursor对象
        self.cursor = self.conn.cursor()
        #错误判断
        try:
            #通过excute用sql语句操作数据库
            self.cursor.execute('insert into `museum info table`(muse_ID,muse_Name,muse_Intro,muse_Address,muse_Opentime,muse_price,muse_class,muse_Ename) values("%d",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")'%(item["museumID"],escape_string(item["museumName"]),escape_string(item["introduction"]),escape_string(item["location"]),escape_string(item["time"]),escape_string(item["price"]),escape_string(item["category"]),escape_string(item["museumForName"])))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


#爬虫文件提交的item类型的对象最终会提交给的管道类：优先级高的
