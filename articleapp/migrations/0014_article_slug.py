# Generated by Django 3.1.5 on 2021-02-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0013_auto_20210203_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]
