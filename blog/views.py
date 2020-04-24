from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

from blog.models import Post


def index(request):
    # return HttpResponse("欢迎访问我的博客首页")
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})
