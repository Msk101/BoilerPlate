# Generated by Django 3.0 on 2021-01-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0002_auto_20210130_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='document_url',
            field=models.FileField(max_length=255, null=True, upload_to=''),
        ),
    ]
