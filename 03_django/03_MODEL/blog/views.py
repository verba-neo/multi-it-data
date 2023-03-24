from django.shortcuts import render

from .models import Article

def new(request):
    pass


def create(request):
    pass


def index(request):
    articles = Article.objects.all()
    
    return render(request, 'blog/index.html', {
        'articles': articles,
    })


# article_pk: var routing 으로 넘어온 값
def detail(request, article_pk): 

    article = Article.objects.get(pk=article_pk)

    return render(request, 'blog/detail.html', {
        'article': article,
    })