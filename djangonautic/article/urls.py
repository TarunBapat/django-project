from django.urls import path,re_path
from . import views

app_name='articles'

urlpatterns = [  
    path('about/',views.about,name="list"),
    re_path(r'^(?P<slug>[\w-]+)/$',views.article_details,name="detail")
   
]