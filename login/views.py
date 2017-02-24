from django.shortcuts import render
from .models import Post


# Create your views here.

#in this function  we are rendering any html file
#when ever this function is called it redirects to post_list.htnl file

def post_list(request): #in login urls.py we call post_list and it takes to views.py i.e, this file
    posts = Post.objects.order_by('published_date') #we create a variable for post in models
    return render(request, 'login/post_list.html', {'posts':posts}) #here this posts variable is rendered to html file