from django.db import models


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