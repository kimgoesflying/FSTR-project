# Generated by Django 4.1 on 2022-08-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mountain_pass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='autumn',
            field=models.CharField(choices=[('1', '1А'), ('2', '1Б'), ('3', '1Б*'), ('4', '2А'), ('5', '2Б*'), ('6', '2Б'), ('7', '3А'), ('8', '3Б'), ('9', '3Б*')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='level',
            name='spring',
            field=models.CharField(choices=[('1', '1А'), ('2', '1Б'), ('3', '1Б*'), ('4', '2А'), ('5', '2Б*'), ('6', '2Б'), ('7', '3А'), ('8', '3Б'), ('9', '3Б*')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='level',
            name='summer',
            field=models.CharField(choices=[('1', '1А'), ('2', '1Б'), ('3', '1Б*'), ('4', '2А'), ('5', '2Б*'), ('6', '2Б'), ('7', '3А'), ('8', '3Б'), ('9', '3Б*')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='level',
            name='winter',
            field=models.CharField(choices=[('1', '1А'), ('2', '1Б'), ('3', '1Б*'), ('4', '2А'), ('5', '2Б*'), ('6', '2Б'), ('7', '3А'), ('8', '3Б'), ('9', '3Б*')], default='', max_length=1),
        ),
    ]
