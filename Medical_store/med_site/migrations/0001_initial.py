# Generated by Django 4.2.7 on 2023-11-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=200)),
                ('doc_spec', models.TextField(help_text='Enter a doctors specialization', max_length=250)),
                ('dep_name', models.CharField(help_text='Enter the department', max_length=100, verbose_name='department')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=200)),
                ('purpose', models.TextField(help_text='Enter a brief description', max_length=200)),
                ('unit', models.CharField(help_text='Enter the unit of Med', max_length=100, verbose_name='Unit')),
                ('dosage', models.CharField(help_text='Dosage of Med', max_length=100, verbose_name='dosage')),
                ('stock', models.IntegerField(blank=True, help_text='Availability', null=True, verbose_name='available')),
            ],
        ),
    ]
