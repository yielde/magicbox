# Generated by Django 3.2.14 on 2022-08-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_rename_tag_healthinfo_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthinfo',
            name='text',
            field=models.IntegerField(choices=[(1, '轻微'), (2, '中等'), (3, '严重')], default=3, verbose_name='疼痛等级'),
        ),
    ]