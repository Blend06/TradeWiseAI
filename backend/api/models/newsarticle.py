from django.db import models
from api.models.cryptoasset import CryptoAsset

class NewsArticle(models.Model):
    NewsArticleId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    source = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    url = models.URLField()
    crypto_asset = models.ForeignKey(CryptoAsset, on_delete=models.CASCADE)

    def __str__(self):
        return self.title