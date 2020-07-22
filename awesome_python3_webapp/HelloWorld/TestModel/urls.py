from django.urls import re_path,path
from TestModel import views

urlpatterns = [
        re_path(r'^test/$',views.test,name='test'),
]
