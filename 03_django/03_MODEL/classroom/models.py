# classroom/models.py
from django.db import models


# 1 model class : 1 DB table
class Student(models.Model):
    # 1 class var : 1 column
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    major = models.CharField(max_length=20)
    phone = models.TextField()

    def __str__(self):
        return f'({self.pk}) => {self.name}'


# class Product(models.Model):
#     pass





# if __name__ == '__main__':
#     # CRUD operations
#     # 생성 Create

#     # 1 instance : 1 record
#     s1 = Student()
#     s1.name = '유태영'
#     s1.age = 20
#     s1.major = '컴퓨터공학'
#     s1.phone = '01012345678'
#     s1.save()

#     s2 = Student(name='김재석', age=30, major='심리학', phone='01054352344')
#     s2.save()

#     Student.objects.create(name='오창희', age=29, major='SW', phone='01051298287')

#     # 조회 Read/Retrieve
#     # 레코드 전체조회
#     Student.objects.all()
#     # 레코드 단일조회 (id==1)
#     s1 = Student.objects.get(pk=1)
#     # 레코드의 컬럼별 조회
#     s1.name
#     s1.age
#     s1.major

#     # 수정 Update => 모든 레코드의 모든 컬럼 수정가능. id는 수정하면 안됨!
#     # '특정' 레코드를 선택하여, 원하는 값을 수정하고, 저장한다.
#     s2 = Student.objects.get(pk=2)
#     s2.major = '경영학'
#     s2.save()

#     # 삭제 Delete
#     # '특정' 레코드를 선택하여, 삭제한다.
#     s3 = Student.objects.get(pk=3)
#     s3.delete()