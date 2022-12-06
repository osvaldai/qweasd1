# Generated by Django 4.1.2 on 2022-10-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bot', '0005_alter_signal_entry_price_alter_signal_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='closing_price',
            field=models.FloatField(default=1.0, max_length=25, verbose_name='Closing Price'),
        ),
        migrations.AlterField(
            model_name='signal',
            name='size',
            field=models.FloatField(default=1.0, max_length=55, verbose_name='Size'),
        ),
    ]