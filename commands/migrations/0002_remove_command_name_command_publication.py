# Generated by Django 4.2.16 on 2024-12-09 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
        ('commands', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='name',
        ),
        migrations.AddField(
            model_name='command',
            name='publication',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='publications.publication'),
            preserve_default=False,
        ),
    ]