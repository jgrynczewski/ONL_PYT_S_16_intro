# Generated by Django 5.0 on 2023-12-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises_app', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=64, null=True)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'in progress'), (1, 'wait for acceptance'), (2, 'published')])),
                ('emission_start', models.DateField(null=True)),
                ('emission_end', models.DateField(null=True)),
            ],
        ),
    ]
