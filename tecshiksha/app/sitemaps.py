from django.contrib.sitemaps import Sitemap
from app.models import Blog,Workshop,Offer

class PostSitemaps(Sitemap):
    def items(self):
        return Blog.objects.all()
        return Workshop.objects.all()
        return Offer.objects.all()
