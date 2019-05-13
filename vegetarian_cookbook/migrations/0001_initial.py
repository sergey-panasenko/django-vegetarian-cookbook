# Generated by Django 2.0 on 2018-03-15 11:12

from django.db import migrations, models
import django.db.models.deletion
#import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='categoty name')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'verbose_name': 'category',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='ingredient name')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='image')),
                #('description', tinymce.models.HTMLField(blank=True, verbose_name='description')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('energy', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='energy')),
                ('protein', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='protein')),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='carbohydrate')),
                ('fat', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='fat')),
            ],
            options={
                'verbose_name_plural': 'ingredients',
                'verbose_name': 'ingredient',
            },
        ),
        migrations.CreateModel(
            name='IngredientUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.DecimalField(decimal_places=4, default=1, max_digits=10, verbose_name='ratio')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vegetarian_cookbook.Ingredient', verbose_name='ingredient')),
            ],
            options={
                'verbose_name_plural': 'additional units',
                'verbose_name': 'additional unit',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('url', models.CharField(blank=True, default='', max_length=250, unique=True, verbose_name='recipe url')),
                ('status', models.CharField(choices=[('P', 'published'), ('d', 'draft'), ('i', 'idea')], default='i', max_length=2, verbose_name='status')),
                #('description', tinymce.models.HTMLField(blank=True, verbose_name='description')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('time', models.IntegerField(blank=True, default=0, null=True, verbose_name='time')),
                ('weight', models.IntegerField(blank=True, default=0, verbose_name='weight')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vegetarian_cookbook.Category', verbose_name='category')),
            ],
            options={
                'verbose_name_plural': 'recipes',
                'verbose_name': 'recipe',
            },
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images', verbose_name='image')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='title')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vegetarian_cookbook.Recipe', verbose_name='recipe')),
            ],
            options={
                'verbose_name_plural': 'images',
                'verbose_name': 'image',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(blank=True, default=0, null=True, verbose_name='weight in gram')),
                ('quantity', models.DecimalField(decimal_places=4, default=0, max_digits=7, verbose_name='quantity on additional unit')),
                ('roughly', models.BooleanField(default=False, verbose_name='roughly')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vegetarian_cookbook.Ingredient', verbose_name='ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vegetarian_cookbook.Recipe', verbose_name='recipe')),
            ],
            options={
                'verbose_name_plural': 'ingredients',
                'verbose_name': 'ingredient',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='tag name')),
            ],
            options={
                'verbose_name_plural': 'tags',
                'verbose_name': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='unit name')),
            ],
            options={
                'verbose_name_plural': 'units',
                'verbose_name': 'unit',
            },
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='unit',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vegetarian_cookbook.Unit', verbose_name='additional unit'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='tags', to='vegetarian_cookbook.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='ingredientunit',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='vegetarian_cookbook.Unit', verbose_name='unit'),
        ),
    ]
