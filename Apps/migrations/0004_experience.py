# Generated by Django 4.1.6 on 2023-07-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0003_alter_education_fieldofstudy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('experience_id', models.AutoField(primary_key=True, serialize=False)),
                ('jobtitle', models.CharField(max_length=256)),
                ('companyname', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('fromdate', models.DateField(blank=True)),
                ('todate', models.DateField(blank=True)),
                ('iscurrentjob', models.BooleanField(default=False)),
            ],
        ),
    ]
