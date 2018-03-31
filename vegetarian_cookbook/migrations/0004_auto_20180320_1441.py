# Generated by Django 2.0 on 2018-03-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetarian_cookbook', '0003_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='carbohydrate',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True, verbose_name='carbohydrate'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='energy',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True, verbose_name='energy'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fat',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True, verbose_name='fat'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='protein',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True, verbose_name='protein'),
        ),
        migrations.AlterField(
            model_name='ingredientnutritionalvalue',
            name='value',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='quantity on additional unit'),
        ),
    ]