# Generated by Django 2.0 on 2018-03-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetarian_cookbook', '0002_auto_20180320_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='image'),
        ),
    ]