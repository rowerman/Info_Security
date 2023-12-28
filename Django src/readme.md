1. 修改 models.py 和 views.py 中的 table 名称
2. 修改 settings.py 中的数据库配置
3. python manage.py makemigrations
4. python manage.py migrate --fake
（3、4两步不一定必需，可以试试不执行）
5. python manage.py runserver
6. 浏览器访问 https://127.0.0.1:8000/info/list