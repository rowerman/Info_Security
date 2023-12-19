# -*- coding: utf-8 -*-
import re

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
    'cookie': 'SINAGLOBAL=9631845029995.297.1676735048156; UOR=,,www.bing.com; XSRF-TOKEN=2pG6TJB5VZ0MgbRKBaOi3mj6; PC_TOKEN=8c49a3e73f; login_sid_t=89cb5caf0ad05772a0d91a0731f305a6; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=weibo.com; Apache=1627802463616.4011.1702883941289; ULV=1702883941291:22:4:2:1627802463616.4011.1702883941289:1702831362390; wb_view_log=1707*10671.5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFYn_Uop81_.LblsFYlAKkY5JpX5o275NHD95QN1h2XSh50eo-7Ws4Dqc_Fi--NiK.Ri-2ci--fi-z7i-i2i--NiKnpi-8si--RiKyWi-zpi--fiKysiKnRi--Xi-zRiKn7i--fi-88i-zfdN9a; SSOLoginState=1702884021; SCF=AtshoCVqgtUwmYD3rHtGD5FWJVP_nHcTmjApJMlH6gz3RWAt15VQicFZuFVpkYrLU5VV9Z3N0z1LtspgOV0d_LQ.; SUB=_2A25Ie4LlDeRhGeFG6lYV8C3OzjyIHXVr-JotrDV8PUNbmtANLRX7kW9NflWw_mihTDgVAb5r_p755mShMKuDR6Al; ALF=1734420020; WBPSESS=sE6oiyQ0pAHUazq0oCGScol415VrDfXV-IPvp9mH5mWtGQRUSrSmd2gKueLDnBbCAxuzUsd7koSfFTo-nr4JyZQ_aKL-i87v1EcPFrnJwElwngpR9PkSqxFzQo27QizLE5qPZdvaLscKKKUK7uRTvA=='
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    # 'weibo.pipelines.CsvPipeline': 301,
    'weibo.pipelines.MysqlPipeline': 302,
    # 'weibo.pipelines.MongoPipeline': 303,
    # 'weibo.pipelines.MyImagesPipeline': 304,
    # 'weibo.pipelines.MyVideoPipeline': 305
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
KEYWORD_LIST = ['原神 雷电将军']  # 或者 KEYWORD_LIST = 'keyword_list.txt'
# 去除每个元素中间的空格
KEYWORD_LIST = [re.sub(r'\s+', '', keyword) for keyword in KEYWORD_LIST]
keywords = '_'.join(KEYWORD_LIST)
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 1
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用“全部”
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2023-12-18'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2023-12-19'
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
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'weibo'
