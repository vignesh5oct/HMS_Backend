# Generated by Django 4.2.23 on 2025-07-23 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_full_name_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_doctor',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_patient',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pregnant', models.BooleanField(default=False)),
                ('pregnancy_term', models.IntegerField(blank=True, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight_unit', models.CharField(choices=[('kg', 'kg')], default='kg', max_length=3)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height_unit', models.CharField(choices=[('cm', 'cm'), ('ft', 'ft')], default='cm', max_length=3)),
                ('age', models.IntegerField()),
                ('blood_group', models.CharField(choices=[('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+')], max_length=3)),
                ('heart_rate', models.CharField(max_length=10)),
                ('bp', models.CharField(max_length=10)),
                ('glucose', models.CharField(max_length=10)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('has_conditions', models.BooleanField(default=False)),
                ('conditions', models.JSONField(blank=True, null=True)),
                ('takes_medicine', models.BooleanField(default=False)),
                ('medicines', models.JSONField(blank=True, null=True)),
                ('self_covered', models.BooleanField(default=True)),
                ('spouse_covered', models.BooleanField(default=False)),
                ('child_count', models.IntegerField(default=0)),
                ('mother_covered', models.BooleanField(default=False)),
                ('father_covered', models.BooleanField(default=False)),
                ('child_1_age', models.IntegerField(blank=True, null=True)),
                ('child_1_image', models.ImageField(blank=True, null=True, upload_to='patient_docs/')),
                ('spouse_age', models.IntegerField(blank=True, null=True)),
                ('spouse_file', models.ImageField(blank=True, null=True, upload_to='patient_docs/')),
                ('father_age', models.IntegerField(blank=True, null=True)),
                ('father_file', models.ImageField(blank=True, null=True, upload_to='patient_docs/')),
                ('mother_age', models.IntegerField(blank=True, null=True)),
                ('mother_file', models.ImageField(blank=True, null=True, upload_to='patient_docs/')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_registered', models.BooleanField(default=False, verbose_name='is registered')),
                ('register_years', models.PositiveIntegerField(blank=True, null=True, verbose_name='years registered')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='clinic address')),
                ('address2', models.CharField(blank=True, max_length=255, verbose_name='address line 2')),
                ('zipcode', models.CharField(blank=True, max_length=10, verbose_name='pincode/zipcode')),
                ('qualification_certificate', models.FileField(blank=True, null=True, upload_to='certificates/')),
                ('photo_id', models.FileField(blank=True, null=True, upload_to='ids/')),
                ('clinical_employment', models.FileField(blank=True, null=True, upload_to='employment_docs/')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='weight')),
                ('weight_unit', models.CharField(default='kg', max_length=10)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='height')),
                ('height_unit', models.CharField(choices=[('cm', 'cm'), ('ft', 'ft')], default='cm', max_length=10)),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='age')),
                ('blood_group', models.CharField(blank=True, choices=[('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+')], max_length=3)),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='city')),
                ('state', models.CharField(blank=True, max_length=100, verbose_name='state')),
                ('specialization', models.CharField(blank=True, max_length=100, verbose_name='specialization')),
                ('experience_years', models.PositiveIntegerField(default=0, verbose_name='years of experience')),
                ('bio', models.TextField(blank=True, verbose_name='biography')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
