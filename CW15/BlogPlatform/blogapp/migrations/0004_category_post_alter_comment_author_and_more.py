# Generated by Django 4.2.3 on 2023-07-14 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('blogapp', '0003_alter_post_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blogapp.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author'),
        ),
    ]