# Generated by Django 4.2.5 on 2024-05-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_item_is_swap_alter_item_image_alter_item_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена'),
        ),
    ]