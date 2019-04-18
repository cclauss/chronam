from __future__ import absolute_import

from django.conf import settings
from django.core.management.base import BaseCommand
from solr import SolrConnection


class Command(BaseCommand):
    help = "send a commit message to the solr index"

    def handle(self, **options):
        solr = SolrConnection(settings.SOLR)
        solr.commit()
