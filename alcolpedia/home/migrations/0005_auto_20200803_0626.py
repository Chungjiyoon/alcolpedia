# Generated by Django 3.0.8 on 2020-08-03 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20200803_0626'),
        ('home', '0004_auto_20200801_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Profile'),
        ),
    ]
