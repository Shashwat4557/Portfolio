# Generated by Django 2.2.7 on 2024-05-06 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20240503_1352'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='service',
        ),
        migrations.DeleteModel(
            name='Testimony',
        ),
        migrations.RemoveField(
            model_name='author',
            name='skills',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
