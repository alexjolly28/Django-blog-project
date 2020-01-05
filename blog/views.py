from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'alex',
        'title': 'blog post 1',
        'content': '1st post content',
        'date_posted': 'dec-28,2018'
    },
    {
        'author': 'neenu',
        'title': 'blog post 2',
        'content': '2st post content',
        'date_posted': 'dec-29,2018'
    }

]


def home(request):
    context= {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
