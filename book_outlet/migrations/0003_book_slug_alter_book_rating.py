# Generated by Django 4.2.4 on 2023-08-19 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_book_author_book_is_bestselling_alter_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
