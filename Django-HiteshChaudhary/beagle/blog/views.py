from django.shortcuts import render,get_object_or_404
from .models import Blogs
# Create your views here.


def Blog(request):
    blog_list = Blogs.objects.all()
    return render(request,"blog.html",{"blogs_list":blog_list})


def Blog_description(request,blogid):
    desc = get_object_or_404(Blogs,pk=blogid)
    return render(request, 'blog_detail.html', {"desc":desc})