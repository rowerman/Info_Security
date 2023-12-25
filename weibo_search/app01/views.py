from django.shortcuts import render, HttpResponse
from .models import YourModel
from django.apps import apps
import pymysql
from decimal import Decimal

def info_list(request, word):
    db = pymysql.connect(host='localhost', user='root', password='123456', database='weibo')
    cursor = db.cursor()
    # 获取表名叫word的表的数据量
    cursor.execute('select * from %s'%word)
    data = cursor.fetchall()

    # 统计每个表不同ip值的数量，将值和数量存进ip_data
    cursor.execute('select ip, count(*) from %s group by ip'%word)
    ip_data = cursor.fetchall()
    # 关闭数据库连接
    db.close()

    return render(request, 'info_list.html', {'data': data, 'ip_data': ip_data})

def heat(request):
    
    # 计算每个表的数据量，进行排序
    data = []
    db = pymysql.connect(host='localhost', user='root', password='123456', database='weibo')
    cursor = db.cursor()
    # 遍历数据库里的所有表名，存进tables_list
    cursor.execute('show tables')
    tables_list = [i[0] for i in cursor.fetchall()]
    for table_name in tables_list:
        # 计算每个表的数据量
        cursor.execute('select count(*) from %s'%table_name)
        count = cursor.fetchone()[0]
        # 计算每个表 attitudes_count 总和
        cursor.execute('select sum(attitudescount) from %s'%table_name)
        attitudes_count = cursor.fetchone()[0]
        # 计算每个表 comments_count 总和
        cursor.execute('select sum(commentscount) from %s'%table_name)
        comments_count = cursor.fetchone()[0]
        # 计算每个表 reposts_count 总和
        cursor.execute('select sum(repostscount) from %s'%table_name)
        reposts_count = cursor.fetchone()[0]

        print(count, attitudes_count, comments_count, reposts_count)

        # 热度评分
        score = Decimal(count)*4/10 + attitudes_count*1/10 + comments_count*2/10 + reposts_count*3/10
        data.append([table_name, score])
    # 对data进行排序
    data.sort(key=lambda x:x[1], reverse=True)
    # 关闭数据库连接
    db.close()

    return render(request, 'heat.html', {'data': data})






