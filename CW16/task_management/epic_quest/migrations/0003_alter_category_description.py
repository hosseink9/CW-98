# Generated by Django 4.2.3 on 2023-07-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic_quest', '0002_remove_category_task_remove_tag_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
