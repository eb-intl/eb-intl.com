from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleList(ListView):
    model = Article
    queryset = Article.objects.order_by('-created')


class ArticleDetail(DetailView):
    model = Article

