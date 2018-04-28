# Generated by Django 2.0 on 2018-04-14 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vegetarian_cookbook', '0010_auto_20180413_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientnutritionalvalue',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='vegetarian_cookbook.Unit', verbose_name='unit'),
        ),
    ]