# Generated by Django 4.2.5 on 2023-11-03 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts_of_computer_app', '0002_ramfeature_processorfeature_mousefeature_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casefanfeature',
            old_name='case_Fan',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='computercasefeature',
            old_name='computer_case',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='coolerfeature',
            old_name='cooler',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='graphicscardfeature',
            old_name='graphics_card',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='keyboardfeature',
            old_name='keyboard',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='monitorfeature',
            old_name='monitor',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='motherboardfeature',
            old_name='motherboard',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='mousefeature',
            old_name='mouse',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='processorfeature',
            old_name='processor',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='ramfeature',
            old_name='ram',
            new_name='product',
        ),
    ]
