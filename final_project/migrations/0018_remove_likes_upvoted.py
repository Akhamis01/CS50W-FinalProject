# Generated by Django 3.1 on 2020-09-10 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('final_project', '0017_likes_upvoted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='upvoted',
        ),
    ]