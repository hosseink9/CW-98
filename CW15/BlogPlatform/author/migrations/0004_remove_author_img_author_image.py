# Generated by Django 4.2.3 on 2023-07-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_alter_author_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='img',
        ),
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='author_images/'),
        ),
    ]