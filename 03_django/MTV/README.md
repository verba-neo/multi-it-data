# Project : `mtv`

```sh
# 프로젝트 폴더를 만들 위치에서 진행 (git bash)

$ mkdir MTV
$ cd MTV
$ python -m venv venv

# windows
$ source venv/Scripts/activate
# mac
$ source venv/bin/activate

(venv)
$ pip install django==3.2.18 django_extensions

(venv)
$ django-admin startproject mtv .

(venv)
$ code .  # 혹은 MTV 폴더 VScode로 열기

# 1. VScode 에서 Ctrl + Shift + P
# 2. Python: Select Interpreter 메뉴 선택
# 3. ('venv': venv) 선택
# 4. VScode 터미널 재시작 후 (venv) 확인 => 시작하기

```


## App name : `board`

```
MTV/ (Project ROOT)
    ㄴ board/
        ㄴ templates/
            ㄴ board/
                ㄴ new.html
                ㄴ index.html
                ㄴ detail.html
                ㄴ edit.html
        ㄴ urls.py
        ㄴ views.py
        ㄴ models.py
        ㄴ ...
    ㄴ templates/
        ㄴ base.html
    ㄴ mtv/ (master APP)
        ㄴ settings.py
        ㄴ urls.py
    ㄴ manage.py

```

### Model: `Notice`
- `Notice` [공지]
    - `title` : `CharField(200)` [제목]
    - `rank` : `IntegerField()`  [중요도]
    - `content` : `TextField()`  [내용]


### URL conf
- `board/new/` => `views.new`
    - 새로운 공지글을 작성하는 HTML(`<form>`)을 제공
    - `new.html`
- `board/create/` => `views.create`
    - 새로운 공지글에 사용자가 POST로 보낸 데이터를 저장
    - 상세 페이지로 `redirect`
- `board/` => `views.index`
    - 전체 공지글들을 조회하는 HTML을 제공
    - 공지글들은 제목만 표시
    - 상세 페이지로 이동할 수 있는 링크로 구성
    - `index.html`
- `board/1/` => `views.detail`
    - 특정 공지글을 조회하는 HTML을 제공
    - 공지글의 `title`/`content`/`rank`를 보여준다.
    - `detail.html`
- `board/1/edit/` => `views.edit`
    - 특정 공지글을 수정하는 HTML(`<form>`)을 제공
    - 사용자가 기존 내용을 확인할 수 있어야 함
    - `edit.html`
- `board/1/update/` => `views.update`
    - 특정 공지글을 사용자가 POST로 보낸 데이터로 수정
    - 상세 페이지로 `redirect`
- `board/1/delete/` => `views.delete`
    - 특정 게시글을 삭제
    - 목록 페이지로 `redirect`


