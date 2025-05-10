from django.db import models
from api.models.cryptoasset import CryptoAsset

class NewsArticle(models.Model):
    NewsArticleId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title