# Generated by Django 3.0.3 on 2020-05-25 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20200525_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='slug',
        ),
    ]
