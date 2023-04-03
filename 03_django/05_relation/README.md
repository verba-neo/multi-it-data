# Project : `relation`
## App name : `blog`

```
05_RELATION/ (Project ROOT)
    ㄴ blog/ 
        ㄴ templates/
            ㄴ blog/
                ㄴ index.html
                ㄴ detail.html
                ㄴ form.html
        ㄴ urls.py
        ㄴ views.py
        ㄴ models.py
        ㄴ *forms.py*
        ㄴ ...
    ㄴ templates/
        ㄴ base.html
    ㄴ relation/ (master APP)
        ㄴ settings.py
        ㄴ urls.py
    ㄴ manage.py

```

### Model
- `Posting` [글]
    - `title` : `CharField(200)`  [제목]
    - `content` : `TextField()`   [내용]

- `Reply` [댓글]
    - `content` : `CharField(200)` [내용]
    - `posting` : `ForeignKey()`   [FK]



### URL conf
```python
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # blog/create/
    path('create/', views.create_posting, name='create_posting'),
    # blog/
    path('', views.posting_index, name='posting_index'),
    # blog/1/
    path('<int:posting_pk>/', views.posting_detail, name='posting_detail'),
    # blog/1/update/
    path('<int:posting_pk>/update/', views.update_posting, name='update_posting'),
    # blog/1/delete/
    path('<int:posting_pk>/delete/', views.delete_posting, name='delete_posting'),
]
```

### Views
```python
from django.shortcuts import render


def create_posting(request):
    pass


def posting_index(request):
    pass


def posting_detail(request, posting_pk):
    pass


def update_posting(request, posting_pk):
    pass


def delete_posting(request, posting_pk):
    pass
```

- Create Posting
    - `GET`
        - 새로운 Posting을 작성하는`form.html`을 제공
    - `POST`
        - 새로운 Posting을 검증 후 저장
        - 상세 페이지로 `redirect`
        - 유효하지 않을 경우, `form.html` 을 render

- Posting Index
    - 전체 Posting들을 조회하는 `index.html`을 제공
    - 상세 페이지로 이동할 수 있는 링크로 구성

- Posting Detail
    - 특정 Posting을 조회하는 `detail.html` 제공
    - Posting의 `title`/`content`를 보여준다.

- Update Posting
    - `GET`
        - 기존 Posting을 수정하는 `form.html`을 제공
    - `POST`
        - 기존 Posting을 검증 후 저장
        - 상세 페이지로 `redirect`
        - 유효하지 않을 경우, `form.html` 을 render

- Delete Posting
    - 특정 Posting을 삭제
    - `POST` 방식으로 접근하도록 만들어야 함
    - 삭제후 목록으로 `rerdirect`
