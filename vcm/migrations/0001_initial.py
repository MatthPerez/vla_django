# Generated by Django 4.2.16 on 2024-11-22 17:04

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
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('song1', models.IntegerField()),
                ('song2', models.IntegerField()),
                ('song3', models.IntegerField()),
                ('portion', models.CharField(max_length=150)),
                ('jewels_title', models.CharField(max_length=150)),
                ('alloc1_type', models.CharField(choices=[('FIRST_CONTACT', '1er contact'), ('RETURN_VISIT', 'Nouvelle visite'), ('BIBLE_STUDY', 'Cours biblique'), ('TALK', 'Discussion'), ('SPEECH', 'Discours'), ('VIDEO', 'Vidéo')], max_length=20)),
                ('alloc2_type', models.CharField(choices=[('FIRST_CONTACT', '1er contact'), ('RETURN_VISIT', 'Nouvelle visite'), ('BIBLE_STUDY', 'Cours biblique'), ('TALK', 'Discussion'), ('SPEECH', 'Discours'), ('VIDEO', 'Vidéo')], max_length=20)),
                ('alloc3_type', models.CharField(blank=True, choices=[('FIRST_CONTACT', '1er contact'), ('RETURN_VISIT', 'Nouvelle visite'), ('BIBLE_STUDY', 'Cours biblique'), ('TALK', 'Discussion'), ('SPEECH', 'Discours'), ('VIDEO', 'Vidéo')], max_length=20, null=True)),
                ('alloc4_type', models.CharField(blank=True, choices=[('FIRST_CONTACT', '1er contact'), ('RETURN_VISIT', 'Nouvelle visite'), ('BIBLE_STUDY', 'Cours biblique'), ('TALK', 'Discussion'), ('SPEECH', 'Discours'), ('VIDEO', 'Vidéo')], max_length=20, null=True)),
                ('alloc1_duration', models.IntegerField()),
                ('alloc2_duration', models.IntegerField()),
                ('alloc3_duration', models.IntegerField(blank=True, null=True)),
                ('alloc4_duration', models.IntegerField(blank=True, null=True)),
                ('vcm1_duration', models.IntegerField()),
                ('vcm2_duration', models.IntegerField(blank=True, null=True)),
                ('vcm3_duration', models.IntegerField(blank=True, null=True)),
                ('vcm1_title', models.TextField(max_length=100)),
                ('vcm2_title', models.TextField(blank=True, max_length=100, null=True)),
                ('vcm3_title', models.TextField(blank=True, max_length=100, null=True)),
                ('supervisor', models.TextField(blank=True, max_length=100, null=True)),
                ('special_speech', models.CharField(blank=True, max_length=100, null=True)),
                ('advisor2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_advisor2', to='persons.person')),
                ('advisor3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_advisor3', to='persons.person')),
                ('alloc1inter_hall1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a1i_h1', to='persons.person')),
                ('alloc1inter_hall2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a1i_h2', to='persons.person')),
                ('alloc1pupil_hall1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a1p_h1', to='persons.person')),
                ('alloc1pupil_hall2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a1p_h2', to='persons.person')),
                ('alloc2inter_hall1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a2i_h1', to='persons.person')),
                ('alloc2inter_hall2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a2i_h2', to='persons.person')),
                ('alloc2pupil_hall1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a2p_h1', to='persons.person')),
                ('alloc2pupil_hall2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a2p_h2', to='persons.person')),
                ('alloc3inter_hall1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a3i_h1', to='persons.person')),
                ('alloc3inter_hall2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a3i_h2', to='persons.person')),
                ('alloc3pupil_hall1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a3p_h1', to='persons.person')),
                ('alloc3pupil_hall2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a3p_h2', to='persons.person')),
                ('alloc4inter_hall1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a4i_h1', to='persons.person')),
                ('alloc4inter_hall2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a4i_h2', to='persons.person')),
                ('alloc4pupil_hall1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a4p_h1', to='persons.person')),
                ('alloc4pupil_hall2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a4p_h2', to='persons.person')),
                ('eba', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_eba', to='persons.person')),
                ('eba_reader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_eba_reader', to='persons.person')),
                ('inter0_hall3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a0i_h3', to='persons.person')),
                ('jewels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_jewels', to='persons.person')),
                ('pearls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_pearls', to='persons.person')),
                ('prayer1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_prayer1', to='persons.person')),
                ('prayer2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_prayer2', to='persons.person')),
                ('president', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_president', to='persons.person')),
                ('pupil0_hall3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a0p_h3', to='persons.person')),
                ('pupil_hall3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_a1p_h3', to='persons.person')),
                ('reading1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_reading1', to='persons.person')),
                ('reading2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_reading2', to='persons.person')),
                ('reading3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_reading3', to='persons.person')),
                ('vcm1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_vcm1', to='persons.person')),
                ('vcm2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_vcm2', to='persons.person')),
                ('vcm3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meetings_as_vcm3', to='persons.person')),
            ],
        ),
    ]
