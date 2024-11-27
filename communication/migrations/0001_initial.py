# Generated by Django 4.2.16 on 2024-11-26 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('CONGREGATION', 'Assemblée locale'), ('CONVENTION', 'Assemblée'), ('MAIL', 'Courrier'), ('LINK', 'Lien Internet'), ('MISCELLANEOUS', 'Divers')], max_length=60)),
                ('content1', models.TextField(max_length=255)),
                ('content2', models.TextField(max_length=255)),
                ('content3', models.TextField(max_length=255)),
            ],
        ),
    ]
