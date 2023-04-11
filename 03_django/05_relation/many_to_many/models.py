from django.db import models

# Example 1
class Artist(models.Model):
    name = models.CharField(max_length=300)
    debut = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f'{self.pk}: {self.name}'


class Album(models.Model):
    title = models.CharField(max_length=300)
    release_date = models.DateField()
    sell_amount = models.PositiveIntegerField()
    artists = models.ManyToManyField(Artist, related_name='albums')  # album_set => albums 로 바꿈

    def __str__(self):
        return f'{self.id}: {self.title}'


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.title}'
    
'''
ar1 = Artist.objects.get(pk=1)
ar2 = Artist.objects.get(pk=2)

al1 = Album.objects.get(pk=4)

al1.artists.add(ar1)
al1.artists.add(ar2)

al1.artists.remove(ar2)

al1.artists.all()  # 앨범1에 참여한 모든 아티스트

ar1.album_set.all()  # 아티스트1이 참여한 모든 앨범

# ar1.albums.all()  => 이걸로 바꾸고 싶다.. => related_name 설정
'''

# Example 2
class Lecture(models.Model):
    title = models.CharField(max_length=200)
    room = models.CharField(max_length=10)


class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=10)
    lectures = models.ManyToManyField(Lecture, through='Enrollment', related_name='students')


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    semester = models.CharField(max_length=200)
    grade = models.CharField(max_length=10)

'''
s1 = Student.objects.create(name='AAA', major='컴공')

s2 = Student.objects.create(name='BBB', major='심리')

s3 = Student.objects.create(name='CCC', major='경영')

l1 = Lecture.objects.create(title='자료구조', room='s101')

l2 = Lecture.objects.create(title='알고리즘', room='s102')

l3 = Lecture.objects.create(title='파이썬', room='s132')

l4 = Lecture.objects.create(title='마케팅원론', room='m112')

e1 = Enrollment.objects.create(student=s1, lecture=l1, grade='A+', semseter='2023-1')

s1.lectures.all()  # => l1
l1.students.all()  # => s1
s1.enrollment_set.all()  # 수강신청 목록
Enrollment.objects.filter(student=s1, semester='2023-1')  # s1 학생의 2023-1학기 모든 수강신청 내역

'''
