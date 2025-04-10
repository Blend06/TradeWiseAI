from django.db import models

class CryptoAsset(models.Model):
    CryptoAssetId = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=20, decimal_places=8)
    market_cap = models.DecimalField(max_digits=25, decimal_places=2)
    change_24h = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.symbol} - {self.name}"