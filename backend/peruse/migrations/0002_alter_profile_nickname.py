# Generated by Django 5.0 on 2023-12-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peruse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]