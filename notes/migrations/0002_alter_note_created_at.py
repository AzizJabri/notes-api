# Generated by Django 4.0.2 on 2022-05-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
