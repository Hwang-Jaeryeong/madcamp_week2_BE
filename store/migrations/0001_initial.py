# Generated by Django 5.0.1 on 2024-01-06 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(max_length=255)),
                ("remaining_quantity", models.IntegerField()),
                (
                    "detail_name1",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "detail_gram1",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "detail_name2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "detail_gram2",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "detail_name3",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "detail_gram3",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Store",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Price",
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
                ("price", models.IntegerField()),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.menu"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="menu",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="store.store"
            ),
        ),
    ]