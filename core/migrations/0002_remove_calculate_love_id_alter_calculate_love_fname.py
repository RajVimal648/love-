# Generated by Django 4.0.6 on 2023-02-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculate_love',
            name='id',
        ),
        migrations.AlterField(
            model_name='calculate_love',
            name='fname',
            field=models.CharField(max_length=25, primary_key=True, serialize=False),
        ),
    ]