# Generated by Django 4.2.6 on 2023-10-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_editora_nome_alter_editora_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(max_length=255, verbose_name='Descrição'),
        ),
    ]