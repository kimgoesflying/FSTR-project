# Generated by Django 4.1 on 2022-08-19 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mountain_pass', '0004_alter_mountainpass_autumn_alter_mountainpass_spring_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mountainpass',
            old_name='autumn',
            new_name='lvl_autumn',
        ),
        migrations.RenameField(
            model_name='mountainpass',
            old_name='spring',
            new_name='lvl_spring',
        ),
        migrations.RenameField(
            model_name='mountainpass',
            old_name='summer',
            new_name='lvl_summer',
        ),
        migrations.RenameField(
            model_name='mountainpass',
            old_name='winter',
            new_name='lvl_winter',
        ),
    ]