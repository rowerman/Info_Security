from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render, HttpResponse
from .models import YourModel

def info_list(request):
    data = YourModel.objects.all()  # 使用指定的数据库查询数据

    daily_counts = (
        data
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(count=Count('id'))
        .order_by('date')
    )

    return render(request, 'info_list.html', {'data': data, 'daily_counts': daily_counts})



