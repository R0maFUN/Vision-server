# Generated by Django 3.1.6 on 2021-04-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='test@test.com', max_length=40, verbose_name='email'),
            preserve_default=False,
        ),
    ]
