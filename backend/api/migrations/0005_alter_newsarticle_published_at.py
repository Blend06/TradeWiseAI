# Generated by Django 5.1.4 on 2025-05-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_newsarticle_crypto_asset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
