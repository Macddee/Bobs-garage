# Generated by Django 4.2.5 on 2023-10-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('for_all_app', '0005_temp_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]