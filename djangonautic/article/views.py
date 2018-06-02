from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article


def about(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'article/about.html',{'articles':articles})


def article_details(request,slug):
    #return HttpResponse(slug)    
    article=Article.objects.get(slug=slug)
    return render(request,'article/article_detail.html',{'article':article})

