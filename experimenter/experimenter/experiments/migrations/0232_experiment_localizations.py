# Generated by Django 3.2.18 on 2023-04-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0231_nimbusexperiment_proposed_release_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="is_localized",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="nimbusexperiment",
            name="localizations",
            field=models.TextField(blank=True, null=True),
        ),
    ]
