# Generated by Django 3.0.2 on 2020-01-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banana', '0005_auto_20200117_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional',
            name='child_num',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
    ]
