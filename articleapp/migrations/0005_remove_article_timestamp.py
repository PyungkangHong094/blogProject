# Generated by Django 3.1.5 on 2021-01-30 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0004_article_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='timestamp',
        ),
    ]
