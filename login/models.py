from django.db import models

class User(models.Model):
    username = models.CharField('username', max_length=20)
    password = models.CharField('password', max_length=30)
    email    = models.CharField('email', max_length=40)


    def __str__(self):
        return self.username + ':' + self.password

