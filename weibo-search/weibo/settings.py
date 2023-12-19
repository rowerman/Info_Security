# -*- coding: utf-8 -*-

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 10
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': 'PC_TOKEN=67bb3d0d4e; login_sid_t=e543e272edcee7d8227260f2cffb83ee; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=2846898638827.7886.1702883046242; SINAGLOBAL=2846898638827.7886.1702883046242; ULV=1702883046244:1:1:1:2846898638827.7886.1702883046242:; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFik.OrxkOD-XU2KCZ9GUY.5JpX5o275NHD95QcSKBRS0M7eon7Ws4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo-X1hMNehzRe5tt; SSOLoginState=1702883076; SUB=_2A25Ie59VDeRhGeBL71oW9y7OwzyIHXVr-J6drDV8PUNbmtANLVj5kW9NRxyi9I0zrEio6OnBxCh5b2j37yPD8oza; ALF=1734419076'
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
#    'weibo.pipelines.CsvPipeline': 1,
#    'weibo.pipelines.MysqlPipeline': 1,
#    'weibo.pipelines.MongoPipeline': 1,
#    'weibo.pipelines.MyImagesPipeline': 1,
    # 'weibo.pipelines.MyVideoPipeline':
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = ['原神']
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 1
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用“全部”
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '12/4/23'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '12/21/23'
# 进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
# 建议数值大小设置在40到50之间。
FURTHER_THRESHOLD = 46
# 图片文件存储路径
IMAGES_STORE = './'
# 视频文件存储路径
FILES_STORE = './'
# 配置MongoDB数据库
# MONGO_URI = 'localhost'
# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'hanwen'
MYSQL_DATABASE = 'weibo'