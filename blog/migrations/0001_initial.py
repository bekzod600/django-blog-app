# Generated by Django 5.1.3 on 2024-11-21 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Category name')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Category slug')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Tag name')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Tag slug')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=550, verbose_name='Post name')),
                ('body', models.TextField(verbose_name='Post body')),
                ('author', models.CharField(default='Admin', max_length=100, verbose_name='Post author')),
                ('views', models.PositiveIntegerField(default=0)),
                ('published_data', models.DateTimeField(auto_now_add=True, verbose_name='Published time')),
                ('published', models.BooleanField(default=False)),
                ('on_top', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='blog.category')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Comment author')),
                ('comment', models.TextField(verbose_name='Comment text')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Post rating')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='blog.post')),
            ],
        ),
    ]
