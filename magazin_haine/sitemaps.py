from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'despre', 'principala']

    def location(self, item):
        return reverse(item)