from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods

from .models import Posting, Reply
from .forms import PostingForm, ReplyForm


@require_http_methods(['GET', 'POST'])
def create_posting(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save()
            return redirect('blog:posting_detail', posting.pk)
    else:
        form = PostingForm()
    return render(request, 'blog/form.html', {
        'form': form,
    })


@require_safe
def posting_index(request):
    postings = Posting.objects.all()
    return render(request, 'blog/index.html', {
        'postings': postings,
    })


# @require_safe 와 아래는 같음
@require_http_methods(['GET', 'HEAD'])
def posting_detail(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    # 댓글 index도 posting_detail 에서 진행
    replies = posting.reply_set.all()
    # 댓글 create도 posting_detail 에서 진행
    form = ReplyForm()

    return render(request, 'blog/detail.html', {
        'posting': posting,
        'replies': replies,
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    if request.method == 'POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save()
            return redirect('blog:posting_detail', posting.pk)
    else:
        form = PostingForm(instance=posting)
    return render(request, 'blog/form.html', {
        'form': form,
    })


@require_POST
def delete_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    posting.delete()
    return redirect('blog:posting_index')


@require_POST
def create_reply(request, posting_pk):
    p = get_object_or_404(Posting, pk=posting_pk)
    form = ReplyForm(request.POST)

    if form.is_valid():
        reply = form.save(commit=False)  # 저장 멈춰! 
        reply.posting = p
        reply.save()
        return redirect('blog:posting_detail', p.pk)
