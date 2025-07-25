from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('create/',views.index, name="create"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('addarticle/',views.addarticle, name="addarticle"),
    path('article/<int:id>/',views.article, name="article"),
    path('update/<int:id>/',views.edit_article, name="update"),
    path('delete/<int:id>/',views.delete_article, name="delete"),
    path('',views.articles, name="articles"),
    path('comment/<int:id>/',views.addComment, name="comment"),


]
