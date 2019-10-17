# Generated by Django 2.0 on 2018-04-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetarian_cookbook', '0006_tag_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='complexity',
            field=models.IntegerField(choices=[(1, 'еasy'), (2, 'medium'), (3, 'hard')], default=1, verbose_name='complexity'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(blank=True, default=0, help_text='Total time for cooking, in minutes', null=True, verbose_name='time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='weight',
            field=models.IntegerField(blank=True, default=0, help_text='Weight after cooking, in gram', verbose_name='weight'),
        ),
    ]
