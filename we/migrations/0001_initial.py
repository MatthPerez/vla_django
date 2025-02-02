# Generated by Django 4.2.16 on 2024-11-22 17:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0003_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekendMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('song1', models.IntegerField()),
                ('song2', models.IntegerField()),
                ('song3', models.IntegerField()),
                ('foreign_speaker', models.TextField(blank=True, max_length=100, null=True)),
                ('speech_title', models.TextField(blank=True, max_length=150, null=True)),
                ('supervisor', models.TextField(blank=True, max_length=100, null=True)),
                ('special_speech', models.CharField(blank=True, max_length=100, null=True)),
                ('prayer1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_we_prayer1', to='persons.person')),
                ('prayer2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_we_prayer2', to='persons.person')),
                ('president', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_we_president', to='persons.person')),
                ('speaker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_we_speaker', to='persons.person')),
                ('watchtower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_we_watchtower', to='persons.person')),
                ('watchtower_reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_we_watchtower_reader', to='persons.person')),
            ],
        ),
    ]
