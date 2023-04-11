from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count

from .models import Posting, Reply
from .forms import PostingForm, ReplyForm


# 로그인 안하고 글쓰는 URL 접속하고, 뭔가 찾아내기
@login_required
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.user = request.user
            posting.save()
            return redirect('blog:posting_detail', posting.pk)
    else:
        form = PostingForm()
    return render(request, 'blog/form.html', {
        'form': form,
    })


@require_safe
def posting_index(request):
    # Count 는 import 해야함
    postings = Posting.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
    paginator = Paginator(postings, 10)  # 페이지당 10개
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {
        # 'postings': postings,
        'page_obj': page_obj,
    })


@login_required
@require_safe
def posting_feed(request):
    user = request.user
    # Posting 객체들 중에 user(작성자)가 user.stars.all() 의 결과중 있는 모든 것
    postings = Posting.objects.filter(user__in=user.stars.all())
    # Posting 객체들 중에 title(제목)이 'a' 문자열을 포함(__contains)하는 모든 것
    postings = Posting.objects.filter(title__contains='a')
    
    # postings = []
    # for star in user.stars.all():
    #     for posting in star.posting_set.all():
    #         postings.append(posting)

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
    
    is_like = posting.like_users.filter(pk=request.user.pk).exists()
    # button_text = '좋아요 취소' if is_like else '좋아요'
    return render(request, 'blog/detail.html', {
        'posting': posting,
        'replies': replies,
        'form': form,
        'is_like': is_like,
        # 'button_text': button_text,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)

    if request.user != posting.user:
        return redirect('blog:posting_index')

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


@login_required
@require_POST
def delete_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    
    if request.user != posting.user:
        return redirect('blog:posting_index')
        
    posting.delete()
    return redirect('blog:posting_index')


@login_required
@require_POST
def create_reply(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    form = ReplyForm(request.POST)

    if form.is_valid():
        reply = form.save(commit=False)  # 저장 멈춰! 
        reply.posting = posting  # 비어있는 컬럼 => FK
        reply.user = request.user
        reply.save()
    return redirect('blog:posting_detail', posting.pk)
    '''
    else:
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest('댓글 에러')

        return render(request, 'blog/detail.html', {
            form: 'form',
            posting: p,
            relies: p.reply_set.all(),
        })
    '''

@login_required
@require_POST
def delete_reply(request, posting_pk, reply_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)

    if request.user == reply.user:
        reply.delete()
        
    return redirect('blog:posting_detail', posting.pk)


@login_required
@require_POST
def like_posting(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    user = request.user

    # 게시글에 좋아요한 사용자들 목록에 있으면,
    # if user in posting.like_users.all():  
    if posting.like_users.filter(pk=user.pk).exists():  # 최적화
        # 좋아요 취소
        posting.like_users.remove(user)
    # 목록에 없으면
    else:
        # 좋아요 추가
        posting.like_users.add(user)
    return redirect('blog:posting_detail', posting.pk)