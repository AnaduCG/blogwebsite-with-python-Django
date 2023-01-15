from django.shortcuts import render, redirect
from .models import Blog
from .create_post import CreateBlogPost

# Create your views here.


def homePage(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogapp/index.html', context)


def blogPage(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, 'blogapp/blog.html', context)


def createPost(request):
    form = CreateBlogPost()
    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'blogapp/create_post.html', context)


def editPost(request,pk):
    blog = Blog.objects.get(id=pk)
    form = CreateBlogPost(instance=blog)
    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'blogapp/create_post.html', context)
