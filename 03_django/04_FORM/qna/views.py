from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_safe, require_http_methods

from .models import Question
from .forms import QuestionForm


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('qna:detail', question.pk)
    else:
        form = QuestionForm()

    return render(request, 'qna/form.html', {
        'form': form,
    })


@require_safe 
def index(request):
    questions = Question.objects.order_by('-reward')
    return render(request, 'qna/index.html', {
        'questions': questions,
    })


@require_safe
def detail(request, question_pk):
    # question = Question.objects.get(pk=question_pk)
    question = get_object_or_404(Question, pk=question_pk)
    return render(request, 'qna/detail.html', {
        'question': question,
    })


@require_http_methods(['GET', 'POST'])
def update(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return redirect('qna:detail', question.pk)
    else:
        form = QuestionForm(instance=question)

    return render(request, 'qna/form.html', {
        'form': form,
    })



@require_POST
def delete(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    question.delete()
    return redirect('qna:index')



