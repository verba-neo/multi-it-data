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
- `blog/create/` => `views.create_posting`
    - `GET`
        - 새로운 Posting을 작성하는`form.html`을 제공
    - `POST`
        - 새로운 Posting을 검증 후 저장
        - 상세 페이지로 `redirect`
        - 유효하지 않을 경우, `form.html` 을 render

- `blog/` => `views.posting_index`
    - 전체 Posting들을 조회하는 `index.html`을 제공
    - 상세 페이지로 이동할 수 있는 링크로 구성

- `blog/1/` => `views.posting_detail`
    - 특정 Posting을 조회하는 `detail.html` 제공
    - Posting의 `title`/`content`를 보여준다.

- `blog/1/update/` => `views.update_posting`
    - `GET`
        - 기존 Posting을 수정하는 `form.html`을 제공
    - `POST`
        - 기존 Posting을 검증 후 저장
        - 상세 페이지로 `redirect`
        - 유효하지 않을 경우, `form.html` 을 render

- `blog/1/delete/` => `views.delete_posting`
    - 특정 게시글을 삭제
    - `POST` 방식으로 접근하도록 만들어야 함
    - 삭제후 목록으로 `rerdirect`
