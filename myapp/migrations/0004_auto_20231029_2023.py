# Generated by Django 3.2.22 on 2023-10-29 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_purchaseddetails_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseddetails',
            old_name='created_at',
            new_name='purchased_at',
        ),
        migrations.RemoveField(
            model_name='purchaseddetails',
            name='date_of_purchase',
        ),
        migrations.RemoveField(
            model_name='purchaseddetails',
            name='total_products',
        ),
    ]