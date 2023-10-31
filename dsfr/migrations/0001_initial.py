# Generated by Django 3.2.5 on 2021-12-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DsfrConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "header_brand",
                    models.CharField(
                        default="République française",
                        max_length=200,
                        verbose_name="Institution (en-tête)",
                    ),
                ),
                (
                    "header_brand_html",
                    models.CharField(
                        default="République<br />française",
                        max_length=200,
                        verbose_name="Institution avec césure (en-tête)",
                    ),
                ),
                (
                    "footer_brand",
                    models.CharField(
                        default="République française",
                        max_length=200,
                        verbose_name="Institution (pied)",
                    ),
                ),
                (
                    "footer_brand_html",
                    models.CharField(
                        default="République<br />française",
                        max_length=200,
                        verbose_name="Institution avec césure (pied)",
                    ),
                ),
                (
                    "site_title",
                    models.CharField(
                        default="Titre du site",
                        max_length=200,
                        verbose_name="Titre du site",
                    ),
                ),
                (
                    "site_tagline",
                    models.CharField(
                        default="Sous-titre du site",
                        max_length=200,
                        verbose_name="Sous-titre du site",
                    ),
                ),
                (
                    "footer_description",
                    models.TextField(default="", verbose_name="Description"),
                ),
                (
                    "mourning",
                    models.BooleanField(default=False, verbose_name="Mise en berne"),
                ),
                (
                    "accessibility_status",
                    models.CharField(
                        choices=[
                            ("FULL", "complètement"),
                            ("PART", "partiellement"),
                            ("NOT", "non"),
                        ],
                        default="non",
                        max_length=4,
                        verbose_name="Statut de conformité de l’accessibilité",
                    ),
                ),
            ],
            options={
                "verbose_name": "Configuration",
            },
        ),
    ]
