import scrapy
from museum.items import educationItem
#scrapy crawl collection
#scrapy crawl exhiition
#scrapy genspider collection//www.xxx.com
#scrapy genspider exhibition
#scrapy genspider education
class Education9Spider(scrapy.Spider):
    name = 'education136'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qzhjg.cn/html/jy/index.html']

    def parse(self, response):
        item = educationItem()
        #scrapy crawl education136
        name="徽博研学游"
        img="http://www.hzwhbwg.com/upfiles/image/15528711260.jpg"
        cont="随着我国素质教育的全面推进，学生的综合实践活动课越来越受到人们的关注和追捧。其中，研学旅行是研究性学习和旅行体验相结合的校外教育活动和综合实践活动课程，而博物馆因其丰富的文化资源以及独特的文化魅力，渐渐地成为了各类研学旅行的重要目的地之一。黄山市已成为“全国首批研学旅行目的地城市”，中国徽州文化博物馆作为全国唯一全面展现徽州文化的历史文化专题博物馆，吸引了众多大中小学校研学团队前来探秘学习。中国徽州文化博物馆日接待各地各级学生研学团队等观众1500人次以上仍为常态，同学们以班级为单位，在博物馆讲解员和志愿者的带领下，有序地进入各大展厅，欣赏着一件件文物展品，观摩着一处处复古场景，瞻仰着一尊尊人物雕像，聆听着一个个源远流长的徽州历史人文故事，一种肃然起敬的感情油然而生。不少同学纷纷感慨，在中国徽州文化博物馆，琳琅满目、造型各异的展品让人们大开眼界，更为古人精湛的技艺折服。"
        print(name)
        print(img)
        print((cont))