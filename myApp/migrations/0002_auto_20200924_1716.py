# Generated by Django 2.2 on 2020-09-24 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sentimentAnalysis',
            new_name='sentimentAnalyzer',
        ),
        migrations.AlterModelOptions(
            name='sentimentanalyzer',
            options={'verbose_name_plural': 'sentimentAnalyzers'},
        ),
    ]
