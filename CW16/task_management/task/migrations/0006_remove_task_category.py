# Generated by Django 4.2.3 on 2023-07-15 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_remove_task_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
    ]
