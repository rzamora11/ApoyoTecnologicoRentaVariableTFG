# Generated by Django 3.1.4 on 2021-05-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210520_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa_esg',
            name='rango',
            field=models.IntegerField(null=True),
        ),
    ]