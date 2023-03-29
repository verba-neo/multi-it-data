from django.shortcuts import render, redirect

from .models import Student
from .forms import StudentForm


def create(request):
    if request.method == 'GET':
        form = StudentForm()
        
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('detail', student.pk)
        
    return render(request, 'blog/form.html', {
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


def update(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    if request.method == 'GET':
        form = StudentForm(instance=student)
    elif request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            # return redirect(f'/blog/{student.pk}/')
            return redirect('detail', student.pk)

    return render(request, 'blog/form.html', {
        'form': form,
    })


def delete(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    student.delete()
    return redirect('index')