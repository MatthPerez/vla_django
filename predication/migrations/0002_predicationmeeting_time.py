# Generated by Django 4.2.16 on 2024-12-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predicationmeeting',
            name='time',
            field=models.TextField(default='', max_length=10),
            preserve_default=False,
        ),
    ]