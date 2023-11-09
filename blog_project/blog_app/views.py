from django.contrib import messages
from django.contrib.auth.models import User,auth

from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    AllBlogs=Blogs.objects.all()
    context={
        'blogs':AllBlogs,
    }
    print(AllBlogs)
    return render(request,'home.html',context)

def addBlog(request):
    form=blogForm()
    if request.method=='POST':
        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'form':form,
    }
    return render(request,'addblog.html',context)

def likeBlog(request,pk):
    blog=Blogs.objects.get(id=pk)
    blog.likes+=1
    blog.save()
    return redirect('/')


def loginpage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "invalid login")
            return redirect('home')
    else:

        return render(request, "loginpage.html")

def logout(request):
    auth.logout(request)
    return redirect('index')




def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, "username already exists")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
        return redirect('loginpage')

    else:
        return render(request, "signup.html")


