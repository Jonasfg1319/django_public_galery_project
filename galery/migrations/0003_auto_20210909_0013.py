# Generated by Django 3.2.7 on 2021-09-09 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0002_auto_20210907_2021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='images',
            old_name='data',
            new_name='date',
        ),
    ]
