# Generated by Django 5.0.3 on 2024-03-31 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='owwner',
            new_name='owner',
        ),
    ]
