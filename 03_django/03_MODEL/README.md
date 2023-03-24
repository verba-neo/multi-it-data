# Project : Model

## App name : blog

## blog - Model

- `Article`
    - `title` : `CharField(200)`
    - `content` : `TextField()`
    - `created_at` : `DateTimeField()`
    - `updated_at` : `DateTimeField()`

## blog - URL conf
> Uniformed Resource Locator
- `blog/new/`
    - 사용자에게 글을 작성하는 HTML을 제공
    - `new.html`
- `blog/create/`
    - 사용자가 POST로 보낸 데이터를 저장
    - ???
- `blog/`
    - 전체 게시글(article)을 조회하는 HTML을 제공
    - 게시글은 제목만 표시하며, 링크로 구성한다
    - `index.html`
- `blog/??/`
    - 특정 게시글을 조회하는 HTML을 제공
    - 게시글의 제목/내용/작성시간/수정시간을 보여준다.
    - `detail.html`
- `blog/?????/`
    - 특정 게시글을 수정하도록 form을 보여주는 HTML 제공
    - `edit.html`
- `blog/??????/`
    - 사용자가 Form을 통해 제출한 데이터로 특정 게시글을 수정
    - ?????
- `blog/?????/`
    - 특정 게시글을 삭제
    - ????


