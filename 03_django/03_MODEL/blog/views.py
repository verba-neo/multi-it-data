from django.shortcuts import render, redirect

from .models import Article


# 사용자에게 form 이 닮긴 html을 보여줌
def new(request):
    return render(request, 'blog/new.html')


# 새로운 게시글(Article instance)을 생성
def create(request):
    a = Article()
    a.title = request.POST['title']
    a.content = request.POST['content']
    a.save()
    # 상세 페이지로 Redirect
    return redirect(f'/blog/{a.pk}/')


# 게시글 목록을 사용자에게 html로 보여줌
def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {
        'articles': articles,
    })


# 특정 게시글 상세내용을 사용자에게 html로 보여줌
# article_pk: var routing 으로 넘어온 값
def detail(request, x): 
    article = Article.objects.get(pk=x)
    return render(request, 'blog/detail.html', {
        'article': article,
    })


def edit(request, x):
    article = Article.objects.get(pk=x)
    return render(request, 'blog/edit.html', {
        'article': article,
    })


def update(request, x):
    a = Article.objects.get(pk=x)
    a.title = request.POST['title']
    a.content = request.POST['content']
    a.save()
    return redirect(f'/blog/{a.pk}')

    

# 특정 게시글의 삭제 / var routing
def delete(request, x):
    article = Article.objects.get(pk=x)
    article.delete()
    return redirect('/blog/')