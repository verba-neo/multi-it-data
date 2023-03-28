from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm


def create(request):
    if request.method == 'GET':
        form = StudentForm()
        
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/new/')
        
    return render(request, 'blog/new.html', {
        'form': form
    })




def index(request):
    students = Student.objects.order_by('-balance')
    return render(request, 'blog/index.html', {
        'students': students,
    })


def detail(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    return render(request, 'blog/detail.html', {
        'student': student,
    })


def edit(request, stduent_pk):
    return render(request, 'blog/edit.html')


def update(request, student_pk):
    return redirect('')


def delete(request, student_pk):
    return redirect('')