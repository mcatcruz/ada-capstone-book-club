# Generated by Django 4.0.1 on 2022-02-15 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adabookclubapp', '0004_group_book_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
    ]
