from django.urls import path,re_path
from . import views

urlpatterns = [  
    path('about/',views.about),
    re_path(r'^(?P<slug>[\w-]+)/$',views.article_details)
   
]