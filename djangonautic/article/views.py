from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


def about(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'article/about.html',{'articles':articles})


def article_details(request,slug):
    #return HttpResponse(slug)    
    article=Article.objects.get(slug=slug)
    return render(request,'article/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            return redirect('articles:list')
    else:        
        form=forms.CreateArticle()   
    return render(request,'article/article_create.html',{'form':form})