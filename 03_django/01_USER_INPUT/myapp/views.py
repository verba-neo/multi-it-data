from django.shortcuts import render

# myapp/ping/
def ping(request):
    return render(request, 'myapp/ping.html')


def pong(request):
    # 사용자 입력은 
    context = {
        'name': request.GET['myname'],
        'age': request.GET['age'],
        'mbti': request.GET['mbti'],
    }
    return render(request, 'myapp/pong.html', context)
