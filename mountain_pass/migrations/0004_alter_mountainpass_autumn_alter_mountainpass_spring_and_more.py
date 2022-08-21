# Generated by Django 4.1 on 2022-08-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountain_pass', '0003_remove_mountainpass_level_mountainpass_autumn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountainpass',
            name='autumn',
            field=models.CharField(choices=[('0', ''), ('1', '1А'), ('2', '1Б'), ('3', '1Б*'), ('4', '2А'), ('5', '2Б*'), ('6', '2Б'), ('7', '3А'), ('8', '3Б'), ('9', '3Б*')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='mountainpass',
            name='spring',
            field=models.CharField(choices=[('0', ''), ('1', '1А'), ('2', '1Б'), ('3', '1Б*'), ('4', '2А'), ('5', '2Б*'), ('6', '2Б'), ('7', '3А'), ('8', '3Б'), ('9', '3Б*')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='mountainpass',
            name='status',
            field=models.CharField(choices=[('n', 'new'), ('p', 'pending'), ('a', 'accepted'), ('r', 'rejected')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='mountainpass',
            name='summer',
            field=models.CharField(choices=[('0', ''), ('1', '1А'), ('2', '1Б'), ('3', '1Б*'), ('4', '2А'), ('5', '2Б*'), ('6', '2Б'), ('7', '3А'), ('8', '3Б'), ('9', '3Б*')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='mountainpass',
            name='winter',
            field=models.CharField(choices=[('0', ''), ('1', '1А'), ('2', '1Б'), ('3', '1Б*'), ('4', '2А'), ('5', '2Б*'), ('6', '2Б'), ('7', '3А'), ('8', '3Б'), ('9', '3Б*')], default='0', max_length=1),
        ),
    ]