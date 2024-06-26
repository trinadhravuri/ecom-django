# Generated by Django 5.0.4 on 2024-04-12 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_articles'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
