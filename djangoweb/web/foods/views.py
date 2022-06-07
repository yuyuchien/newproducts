from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import foodsList

def foods(request):
    data = foodsList.objects.all()
    content = {'foods':data}
    return render(request,'foods.html',content)