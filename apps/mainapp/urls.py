from django.conf.urls import url, include
from apps.mainapp import views 
from django.urls import path, re_path

app_name = 'mainapp'
urlpatterns = [  

    # daily diet 
    url(r'^(?P<name>\w+)$', views.hello), 

]  о