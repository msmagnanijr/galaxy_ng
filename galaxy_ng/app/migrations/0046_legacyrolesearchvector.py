# Generated by Django 4.2.7 on 2023-11-15 15:52

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("galaxy", "0045_setting"),
    ]

    operations = [
        migrations.CreateModel(
            name="LegacyRoleSearchVector",
            fields=[
                (
                    "role",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="galaxy.legacyrole",
                    ),
                ),
                ("search_vector", django.contrib.postgres.search.SearchVectorField(default="")),
                ("modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "indexes": [
                    django.contrib.postgres.indexes.GinIndex(
                        fields=["search_vector"], name="galaxy_lega_search__13e661_gin"
                    )
                ],
            },
        ),
    ]
