# Generated by Django 4.0.1 on 2022-02-02 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adabookclubapp', '0005_discussion_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='title',
            new_name='subject',
        ),
    ]
