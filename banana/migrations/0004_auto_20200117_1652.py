# Generated by Django 3.0.2 on 2020-01-17 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banana', '0003_user_chat_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additional',
            name='child',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'yes')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='additional',
            name='marriage',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'yes')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='additional',
            name='parent',
            field=models.CharField(blank=True, choices=[('이혼', '이혼'), ('별거', '별거'), ('사망', '사망'), ('해당없음', '해당없음'), ('기타', '기타')], max_length=10, null=True),
        ),
    ]
