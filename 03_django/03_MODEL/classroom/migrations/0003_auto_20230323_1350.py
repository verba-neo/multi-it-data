# Generated by Django 3.2.18 on 2023-03-23 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20230323_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='student',
            name='graduated',
        ),
    ]
