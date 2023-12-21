from django.shortcuts import render, HttpResponse
from .models import YourModel

def info_list(request):
    # table_name = request.GET.get('table_name')  # 从前端获取表名
    table_name = '甘肃'
    data = YourModel.objects.all()  # 使用指定的数据库查询数据

    return render(request, 'info_list.html', {'data': data})



