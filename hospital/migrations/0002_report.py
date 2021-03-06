# Generated by Django 3.0.5 on 2020-09-27 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testName', models.CharField(max_length=40, null=True)),
                ('testDate', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('report_file', models.FileField(blank=True, null=True, upload_to='patient/reports/')),
                ('status', models.BooleanField(default=False)),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Doctor')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Patient')),
            ],
        ),
    ]
