from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$',views.post_list, name= 'post_list'),
    #one view called as post_list is created

]