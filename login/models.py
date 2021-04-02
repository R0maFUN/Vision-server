from django.db import models

class User(models.Model):
    username = models.CharField('username', max_length=20)
    password = models.CharField('password', max_length=30)
    name     = models.CharField('name', max_length=20)


    def __str__(self):
        return self.username + ':' + self.password

