# Generated by Django 5.0.3 on 2024-03-20 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fichiercsv',
            options={'ordering': ['-nom'], 'verbose_name': 'FichierCSV'},
        ),
        migrations.RenameField(
            model_name='fichiercsv',
            old_name='author',
            new_name='file_author',
        ),
    ]
