# Generated by Django 5.1.4 on 2024-12-13 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_product_certificate_product_review_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='product_varities',
            new_name='product_varieties',
        ),
    ]
