# Generated by Django 3.1.5 on 2021-02-02 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0009_auto_20210202_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
