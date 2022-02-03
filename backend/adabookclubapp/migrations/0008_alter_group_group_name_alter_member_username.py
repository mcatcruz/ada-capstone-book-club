# Generated by Django 4.0.1 on 2022-02-02 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adabookclubapp', '0007_alter_discussion_subject_alter_group_group_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(help_text='Enter a group name', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(help_text='Enter a username', max_length=30, unique=True),
        ),
    ]
