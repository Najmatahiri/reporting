# Generated by Django 5.0.3 on 2024-03-27 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_machinevm_fichier_csv_alter_fichiercsv_contenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinevm',
            name='slug',
        ),
    ]
