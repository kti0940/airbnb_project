# Generated by Django 4.1.2 on 2022-10-27 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_host",
            field=models.BooleanField(default=False),
        ),
    ]
