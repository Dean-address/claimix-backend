# Generated by Django 5.2.4 on 2025-07-13 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy_holder', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='policy_subscription',
            new_name='PolicySubscription',
        ),
        migrations.AlterModelOptions(
            name='policy',
            options={'verbose_name': 'Policy', 'verbose_name_plural': 'Policies'},
        ),
        migrations.AlterModelOptions(
            name='policyholder',
            options={'verbose_name': 'PolicyHolder', 'verbose_name_plural': 'PoliciesHolders'},
        ),
        migrations.AlterModelOptions(
            name='policysubscription',
            options={'verbose_name': 'PolicySubscription', 'verbose_name_plural': 'PoliciesSubscription'},
        ),
    ]
