from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.forms import PostForm
from posts.models import Post


def main_veiw(request):
    if request.method == 'GET':
        return render(request, "base.html")
def hello_view(request):
    return HttpResponse("Hello World!")

def html_view(request):
    return render(request, "base.html")

def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, "posts/list_view.html", context={"posts": posts})

def details_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, "posts/detail_view.html", context={"post": post})

def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, "posts/posts_create.html", context={"form": form})

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/posts/")
        return render(request, "posts/posts_create.html", context={"form": form})
