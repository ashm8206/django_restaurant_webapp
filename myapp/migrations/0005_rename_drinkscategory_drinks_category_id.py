# Generated by Django 4.2.14 on 2024-07-26 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_drinks_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinks',
            old_name='DrinksCategory',
            new_name='category_id',
        ),
    ]
