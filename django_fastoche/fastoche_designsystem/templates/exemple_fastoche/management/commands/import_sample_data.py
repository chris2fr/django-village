from django.core.management.base import BaseCommand

from fastoche.models import FastocheConfig, FastocheSocialMedia
from example_app.models import Genre


class Command(BaseCommand):
    help = "Add some initial sample data for the example app."

    def handle(self, *args, **options):
        # Note: the command should be able to be run several times without creating
        # duplicate objects.
        config, _created = FastocheConfig.objects.get_or_create(
            language="fr",
            defaults={
                "header_brand": "République française",
                "header_brand_html": "République<br />française",
                "footer_brand": "République française",
                "footer_brand_html": "République<br />française",
                "site_title": "Django-FASTOCHE",
                "site_tagline": "Intégration du système de design de l’État pour les sites utilisant Django",
                "footer_description": '<a href="https://github.com/numerique-gouv/django-fastoche" \r\ntarget="_blank" rel="noreferrer noopener">Dépôt Github</a>',
                "mourning": False,
                "accessibility_status": "NOT",
                "newsletter_description": """Nous n’avons pas de lettre d’information mais vous pouvez trouver
                les dernières publications sur cette page.""",
                "newsletter_url": "https://github.com/numerique-gouv/django_fastoche/releases",
            },
        )

        FastocheSocialMedia.objects.get_or_create(
            site_config=config,
            title="Mastodon",
            url="https://social.numerique.gouv.fr/explore",
            icon_class="fastoche-btn--mastodon",
        )

        Genre.objects.get_or_create(code="SF", designation="Science-Fiction")
        Genre.objects.get_or_create(
            code="FTSQUE",
            designation="Fantastique",
            help_text="Intrusion du surnaturel dans un cadre réaliste",
        )
        Genre.objects.get_or_create(
            code="FTSY",
            designation="Fantasy",
            help_text="Élaboration d’un univers distinct du monde réel",
        )