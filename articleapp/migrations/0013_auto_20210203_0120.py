# Generated by Django 3.1.5 on 2021-02-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0012_auto_20210203_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='article/'),
        ),
    ]