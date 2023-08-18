from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='like')
    date_created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='question_pic', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - Question  {self.likes.count()} - likes'

class Comment(models.Model):
    question = models.ForeignKey(Questions, related_name="comment",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.question.title}, {self.question.user}"




class User_profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000, default="lahore")
    phone = models.IntegerField(null=True, blank=True)
    image = models.ImageField( default='default.jpg', upload_to='profile_pic' )

    def __str__(self):
        return f'{self.user.username} -profile'


class Contact(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    

