# Generated by Django 4.0.5 on 2022-06-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_date_updated_book_image_field_book_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_field',
            field=models.ImageField(default=None, max_length=200, null=True, upload_to='static/'),
        ),
    ]