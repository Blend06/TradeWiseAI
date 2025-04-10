from django.contrib import admin
from api.models.cryptoasset import CryptoAsset
from api.models.newsarticle import NewsArticle
from api.models.chatmessage import ChatMessage
from api.models.userfeedback import UserFeedback
from api.models.user import User
from api.models.watchlist import WatchList

admin.site.register(User)
admin.site.register(CryptoAsset)
admin.site.register(NewsArticle)
admin.site.register(ChatMessage)
admin.site.register(WatchList)
admin.site.register(UserFeedback)
