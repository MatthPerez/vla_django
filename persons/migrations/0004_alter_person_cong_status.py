# Generated by Django 4.2.16 on 2024-12-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cong_status',
            field=models.CharField(blank=True, choices=[('UNBAPT_PUBLISHER', 'Proclamateur non baptisé'), ('PUBLISHER', 'Proclamateur'), ('TEMPORARY', 'Pionnier auxiliaire'), ('PERMANENT', 'Pionnier permanent'), ('SPECIAL', 'Pionnier spécial')], max_length=16, null=True, verbose_name='Statut'),
        ),
    ]
