from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.new_post_page, name="new_post"),
    path('<slug:slug>', views.single_post_page, name="single_post"),
]
