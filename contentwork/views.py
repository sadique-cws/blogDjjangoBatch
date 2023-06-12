from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post

def home(r):
    data = Post.objects.all()
    return render(r, "home.html",{"postData":data})

def insert(r):
    form = PostForm(r.POST or None)

    if(r.method == "POST"):
        if form.is_valid():
            form.save()
            return redirect(home)
        
    return render(r, "insert.html",{"form":form})