from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    

class Comment(models.Model):
    content = models.CharField(max_length=200)
    # Article 모델의 PK 를 저장/Article 레코드 삭제시, 관련된 모든 Comment 레코드 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # FK의 경우 클래스 변수명 뒤에 _id가 자동으로 붙어서 테이블 컬럼이 됨


'''
a1 = Article.objects.create(title='월요일', content='싫어욥')

c1 = Comment.objects.create(content='맞아맞아', article_id=1)
c2 = Comment.objects.create(content='짱싫다', article_id=a1.id)
c3 = Comment.objects.create(content='난 좋음', article=a1)

# c1 댓글이 달린 게시글
c1.article

# c1 댓글이 달린 게시글의 제목
c1.article.title

# a1에 달린 모든 댓글 (모델명 소문자 + _set)
a1.comment_set.all()  

# a1에 달린 댓글들을 pk 내림차순
a1.comment_set.order_by('-pk')
'''
