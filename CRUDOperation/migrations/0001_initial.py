# Generated by Django 5.0.3 on 2024-03-26 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChimModel",
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
                ("chimcuaai", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=150)),
                ("docong", models.IntegerField()),
                ("dodai", models.IntegerField()),
                ("sizechim", models.CharField(max_length=100)),
            ],
        ),
    ]
