# Generated by Django 4.2.5 on 2025-02-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0011_remove_payment_total_fee_payment_total_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomassign',
            name='food_required',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, help_text='2000 rs for one month', max_length=20),
        ),
    ]
