from django.db import models

class YourModel(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    bid = models.CharField(max_length=12)
    user_id = models.CharField(max_length=20)
    screen_name = models.CharField(max_length=30)
    text = models.CharField(max_length=2000)
    article_url = models.CharField(max_length=100)
    topics = models.CharField(max_length=200)
    at_users = models.CharField(max_length=1000)
    pics = models.CharField(max_length=3000)
    video_url = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    source = models.CharField(max_length=30)
    attitudes_count = models.IntegerField()
    comments_count = models.IntegerField()
    reposts_count = models.IntegerField()
    retweet_id = models.CharField(max_length=20)
    ip = models.CharField(max_length=100)

    class Meta:
        # db_table = 'your_table_name'  # 指定表名，从前端获取
        db_table = '原神迪卢克'  # 指定表名
