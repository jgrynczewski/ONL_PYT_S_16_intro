# Generated by Django 5.0 on 2023-12-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0005_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('rating', models.IntegerField(choices=[(0, '0 stars'), (1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])),
            ],
        ),
    ]
