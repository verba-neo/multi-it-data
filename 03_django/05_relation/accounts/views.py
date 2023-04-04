# accounts/views.py
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


from .forms import CustomUserCreationForm

@require_http_methods(['GET', 'POST'])
def signup(request):
    # create_user
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('blog:posting_index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        # ID/PW 가 맞다면,
        if form.is_valid():
            # 인증을 해줘야 함

            return redirect('blog:posting_index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {
        'form': form,
    })


def signout(request):
    pass
