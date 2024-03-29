# Generated by Django 5.0.3 on 2024-03-08 01:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("content", models.TextField()),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                ("likes", models.PositiveBigIntegerField(default=0)),
                ("reviews", models.PositiveBigIntegerField(default=0)),
                ("writer", models.CharField(max_length=30)),
            ],
        ),
    ]
