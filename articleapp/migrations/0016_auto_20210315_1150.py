# Generated by Django 3.1.5 on 2021-03-15 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0015_article_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'managed': False, 'verbose_name': '사진'},
        ),
    ]