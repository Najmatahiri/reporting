# Generated by Django 5.0.6 on 2024-06-05 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0012_alter_historicalmachinevm_ip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmachinevm',
            name='import_month',
            field=models.CharField(editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='machinevm',
            name='import_month',
            field=models.CharField(editable=False, max_length=10),
        ),
    ]
