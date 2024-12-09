"""
URL configuration for djangoHomeWork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import hello_view, html_view, posts_list_view, main_veiw, details_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_veiw),
    path("hello/", hello_view),
    path("html-viev/", html_view),
    path("posts/", posts_list_view),
    path("posts/<int:post_id>/", details_view),

]
