from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all()
    paginators = Paginator(posts, 50) # show 50 post as page
    page_number = request.GET.get('page')
    page_objs = paginators.get_page(page_number)
    return render(request, "index.html", {'posts': page_objs})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})

def post_search(request):
    if 'search_keyword' in request.GET:
        search_keyword = request.GET['search_keyword']
        posts = Post.objects.filter(title__contains = search_keyword)
        return render(request, 'index.html', {'posts': posts})
    else:
        return redirect('index')