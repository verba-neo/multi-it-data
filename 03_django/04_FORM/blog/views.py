from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm


def new(request):
    form = StudentForm()

    return render(request, 'blog/new.html', {
        'form': form,
    })


def create(request):
    # form 에 사용자 입력 데이터 붙임
    form = StudentForm(request.POST)
    
    # data가 유효하다면,
    if form.is_valid():
        form.save()
        return redirect('/blog/new/')
    # data가 유효하지 않다면
    else:
        return render(request, 'blog/new.html', {
            'form': form
        })
    

def index(request):
    return render(request, 'blog/index.html')


def detail(request, student_pk):
    return render(request, 'blog/detail.html')


def edit(request, stduent_pk):
    return render(request, 'blog/edit.html')


def update(request, student_pk):
    return redirect('')


def delete(request, student_pk):
    return redirect('')