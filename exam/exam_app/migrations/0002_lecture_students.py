# Generated by Django 5.0 on 2023-12-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='students',
            field=models.ManyToManyField(to='exam_app.student'),
        ),
    ]
