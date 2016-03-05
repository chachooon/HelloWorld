from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core.urlresolvers import reverse

from .models import Post
from .models import Category
from .models import Comment
from .models import Tag

def list_posts(request):
    per_page = 5

    current_page = request.GET.get('page',1)
    all_posts = Post.objects.select_related().prefetch_related().all().order_by('-pk')
    pagi = Paginator(all_posts, per_page)
    try:
        pg = pagi.page(current_page)
    except PageNotAnInteger:
        pg = pagi.page(1)
    except EmptyPage:
        pg = []

    # start_offset = (current_page-1) * per_page
    # end_offset = current_page * per_page
    # all_posts = all_posts[start_offset:end_offset]
    return render(request, 'list_posts.html',{
        'posts' : pg,
    })

def view_post(request, pk):
    the_post = get_object_or_404(Post, pk=pk)


    return render(request, 'view_post.html',{
        'post': the_post,
    })

def create_post(request):
    categories = Category.objects.all()

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        new_post = Post()
        new_post.title = request.POST.get('title')
        new_post.content = request.POST.get('content')

        category_pk = request.POST.get('category')
        category = get_object_or_404(Category, pk=category_pk)
        new_post.category = category
        new_post.save()

        return redirect('view_post', pk=new_post.pk)
    return render(request, 'create_post.html',{
        'categories':categories,
    })

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        categories = Category.objects.all()
    else:
        form = request.POST
        category = get_object_or_404(Category, pk=form['category'])
        post.title = form['title']
        post.content = form['content']
        post.category = category
        post.save()
        return redirect('blog:view_post', pk=post.pk)

    return render(request, 'edit_post.html', {
        'post' : post,
        'categories' : categories,
    })

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    if request.method == 'POST': 
        post.delete() 
        return redirect('blog:list_post') 
 
    return render(request, 'delete_post.html', { 
        'post': post, 
    }) 
