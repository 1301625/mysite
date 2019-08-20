from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.contrib import messages
from .forms import PostForm
# Create your views here.
from django.core.paginator import Paginator ,EmptyPage ,PageNotAnInteger

import math

def post_list(request):
    posts = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        posts = posts.filter(title__icontains=q)

    #posts_django = Post.objects.filter(tags__contains='HTTP')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    # page_range= 5
    # current_block  = math.ceil(int(page)/page_range)
    # start_block = (current_block-1) * page_range
    # end_block = start_block + page_range

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request, 'blog/post_list.html', {
        'posts': posts
        , 'q': q,
     #   'posts_django' : posts_django,
    })

def post_tags(request ,tags):
    posts = Post.objects.filter(tags__contains=tags)
    context = {
        'tags':tags,
        'posts':posts
    }
    return render(request, 'blog/post_tags.html' ,context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            messages.success(request, messages.INFO, "새 글이 등록되었습니다")
            post.published_date = timezone.now()
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            messages.success(request, "글이 수정되었습니다")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
