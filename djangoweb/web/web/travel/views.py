from django.shortcuts import render

from .models import travelList

# Create your views here.

def travel(request):
    # id =>欄位名稱
    # order_by('-id')  =>  進行遞減排序
    # order_by('id')  =>  進行遞增排序
    data = travelList.objects.all().order_by('-id')
    content = {'traveldata':data}
    return render(request,'travel.html',content)