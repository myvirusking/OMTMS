# Generated by Django 2.0.4 on 2018-05-04 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_moviename'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviename',
            name='language',
            field=models.CharField(default='Hindi', max_length=10),
        ),
    ]
