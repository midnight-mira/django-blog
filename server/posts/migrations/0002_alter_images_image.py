# Generated by Django 5.0.7 on 2024-08-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="images",
            name="image",
            field=models.ImageField(upload_to="posts"),
        ),
    ]
