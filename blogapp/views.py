from django.shortcuts import render, redirect
from .models import Blog, Message
from .forms import CreateBlogPost,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def homePage(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'blogapp/index.html', context)


def blogPage(request, pk):
    blog = Blog.objects.get(id=pk)
    count = blog.comment_set.count()
    comments = blog.comment_set.all().order_by('-created')[:3]
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            messages.success(request, 'Comment successful')
    context = {'blog': blog,'count':count,'comments':comments,'form':form}
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


def contact(request):
    context = {}
    return render(request,'blogapp/contact.html',context)