# Generated by Django 3.0.8 on 2020-08-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='dated_at',
            new_name='updated_at',
        ),
    ]