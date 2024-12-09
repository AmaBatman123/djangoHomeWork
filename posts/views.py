from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post

def main_veiw(request):
    return render(request, "base.html")
def hello_view(request):
    return HttpResponse("Hello World!")

def html_view(request):
    return render(request, "base.html")

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/list_view.html", context={"posts": posts})

def details_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/detail_view.html", context={"post": post})


