# Generated by Django 4.2.5 on 2023-10-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_all_app', '0006_alter_temp_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temp',
            name='total',
        ),
        migrations.AddField(
            model_name='temp',
            name='order_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
