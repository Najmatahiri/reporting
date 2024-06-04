# Generated by Django 5.0.6 on 2024-05-29 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0005_configversionhs_delete_config'),
    ]

    operations = [
        migrations.CreateModel(
            name='FichierCSV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('date_import', models.DateField(auto_now=True)),
                ('contenu', models.FileField(upload_to='csv_files/')),
            ],
        ),
    ]