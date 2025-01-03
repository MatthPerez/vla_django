# Generated by Django 4.2.16 on 2024-12-05 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_alter_person_cong_status'),
        ('predication', '0002_predicationmeeting_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predicationmeeting',
            old_name='place',
            new_name='place1',
        ),
        migrations.RenameField(
            model_name='predicationmeeting',
            old_name='time',
            new_name='time1',
        ),
        migrations.RemoveField(
            model_name='predicationmeeting',
            name='manager',
        ),
        migrations.AddField(
            model_name='predicationmeeting',
            name='manager1',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='manager1', to='persons.person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predicationmeeting',
            name='manager2',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='manager2', to='persons.person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predicationmeeting',
            name='manager3',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='manager3', to='persons.person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predicationmeeting',
            name='place2',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predicationmeeting',
            name='place3',
            field=models.TextField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predicationmeeting',
            name='time2',
            field=models.TextField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predicationmeeting',
            name='time3',
            field=models.TextField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
