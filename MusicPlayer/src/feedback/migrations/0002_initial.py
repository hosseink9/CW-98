# Generated by Django 4.2.4 on 2023-09-02 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geners', '0001_initial'),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geners.song'),
        ),
    ]
