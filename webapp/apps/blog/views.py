from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleList(ListView):
    model = Article
    paginate_by = 25
    #queryset = Article.objects.filter(publish=True).order_by('-created')


class ArticleDetail(DetailView):
    model = Article

