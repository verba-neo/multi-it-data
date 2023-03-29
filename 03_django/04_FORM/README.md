
# App name : `qna`

```
04_FORM/ (Project ROOT)
    ㄴ blog/  # 우리 기존 실습 코드
    ㄴ qna/
        ㄴ templates/
            ㄴ qna/
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
    ㄴ form/ (master APP)
        ㄴ settings.py
        ㄴ urls.py
    ㄴ manage.py

```

### Model: `Question`
- `Question` [질문]
    - `title` : `CharField(200)`  [제목]
    - `reward` : `IntegerField()` [보상(내공)]
    - `content` : `TextField()`   [내용]


### URL conf
- `qna/create/` => `view.create`
    - `GET`
        - 새로운 질문을 작성하는`form.html`을 제공
    - `POST`
        - 새로운 질문을 검증 후 저장
        - 상세 페이지로 `redirect`
        - 유효하지 않을 경우, `form.html` 을 render

- `qna/` => `views.index`
    - 전체 질문들을 조회하는 `index.html`을 제공
    - 질문 목록은 `reward` 높은것이 위로 보이도록 함.
    - 상세 페이지로 이동할 수 있는 링크로 구성
- `qna/1/` => `views.detail`
    - 특정 질문을 조회하는 `detail.html` 제공
    - 질문의 `title`/`content`/`reward`를 보여준다.
- `qna/1/update/` => `views.update`
    - `GET`
        - 기존 질문을 수정하는 `form.html`을 제공
    - `POST`
        - 기존 질문을 검증 후 저장
        - 상세 페이지로 `redirect`
        - 유효하지 않을 경우, `form.html` 을 render
- `qna/1/delete/` => `views.delete`
    - 특정 게시글을 삭제
    - `POST` 방식으로 접근하도록 만들어야 함
    - 삭제후 목록으로 `rerdirect`
