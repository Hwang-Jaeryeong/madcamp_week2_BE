# Generated by Django 3.2.16 on 2024-01-09 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('remaining_quantity', models.IntegerField()),
                ('detail_name1', models.CharField(blank=True, max_length=255, null=True)),
                ('detail_gram1', models.CharField(blank=True, max_length=255, null=True)),
                ('detail_name2', models.CharField(blank=True, max_length=255, null=True)),
                ('detail_gram2', models.CharField(blank=True, max_length=255, null=True)),
                ('detail_name3', models.CharField(blank=True, max_length=255, null=True)),
                ('detail_gram3', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
    ]
