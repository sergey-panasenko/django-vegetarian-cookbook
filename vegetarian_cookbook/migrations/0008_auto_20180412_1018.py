# Generated by Django 2.0 on 2018-04-12 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetarian_cookbook', '0007_auto_20180412_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='weight',
            field=models.IntegerField(blank=True, default=0, help_text='Weight after cooking, in grams', verbose_name='weight'),
        ),
    ]
