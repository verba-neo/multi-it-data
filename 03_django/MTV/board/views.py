from django.shortcuts import render, redirect

from .models import Notice


def new(request):
    return render(request, 'board/new.html')


def create(request):
    notice = Notice()
    notice.title = request.POST['title']
    notice.rank = request.POST['rank']
    notice.content = request.POST['content']
    notice.save()
    return redirect(f'/board/{notice.pk}/')


def index(request):
    # notices = Notice.objects.all()

    notices = Notice.objects.order_by('-rank')  # rank 컬럼 내림차순 정렬

    return render(request, 'board/index.html', {
        'notices': notices,
    })


def detail(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    return render(request, 'board/detail.html', {
        'notice': notice,
    })


def edit(request, notice_pk):
    # 1. form action에서 /board/notice.pk/update/ 
    # 2. input/textarea 에 기존 내용을 보여주기 위함
    notice = Notice.objects.get(pk=notice_pk)

    return render(request, 'board/edit.html', {
        'notice': notice,
    })


def update(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    notice.title = request.POST['title']
    notice.rank = request.POST['rank']
    notice.content = request.POST['content']
    notice.save()
    return redirect(f'/board/{notice.pk}/')



def delete(request, notice_pk):
    notice = Notice.objects.get(pk=notice_pk)
    notice.delete()
    return redirect('/board/')
