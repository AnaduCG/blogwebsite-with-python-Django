from django.shortcuts import render, redirect
from .models import Blog, Message
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


def editPost(request, pk):
    blog = Blog.objects.get(id=pk)
    form = CreateBlogPost(instance=blog)
    if request.method == 'POST':
        form = CreateBlogPost(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'blogapp/create_post.html', context)


def inbox(request):
    inbox = Message.objects.all().order_by('is_read')
    context = {'inbox': inbox}
    return render(request, 'blogapp/inbox.html', context)


def message(request,pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'blogapp/message.html', context)
