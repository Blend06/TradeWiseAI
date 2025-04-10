from django.db import models

class WatchList(models.Model):
    WatchListid = models.AutoField(primary_key=True)  
    user = models.ForeignKey('api.User', on_delete=models.CASCADE)  # Use string reference for custom User model
    crypto_asset = models.ForeignKey('api.CryptoAsset', on_delete=models.CASCADE)  # Use string reference for CryptoAsset

    def __str__(self):
        return f"{self.user.username} - {self.crypto_asset.symbol}"