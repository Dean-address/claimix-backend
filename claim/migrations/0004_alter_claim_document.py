# Generated by Django 5.2.4 on 2025-07-14 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claim', '0003_claim_created_at_alter_claim_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='document',
            field=models.ImageField(help_text='upload document and images', null=True, upload_to='claims/'),
        ),
    ]
