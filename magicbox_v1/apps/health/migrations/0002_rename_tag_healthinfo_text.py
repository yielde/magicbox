# Generated by Django 3.2.14 on 2022-08-11 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthinfo',
            old_name='tag',
            new_name='text',
        ),
    ]