from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.user_view import UserViewSet

from api.views.chatmessage_view import ChatMessageViewSet
from api.views.cryptoasset_view import CryptoassetViewSet
from api.views.newsarticle_view import NewsarticleViewSet
from api.views.userfeedback_view import UserfeedbackViewSet
from api.views.watchlist_view import WatchlistViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'chatmessage', ChatMessageViewSet)
router.register(r'cryptoasset', CryptoassetViewSet)
router.register(r'newsarticle', NewsarticleViewSet)
router.register(r'userfeedback', UserfeedbackViewSet)
router.register(r'watchlist', WatchlistViewSet)

urlpatterns = [
     path('', include(router.urls)),
     path('api/', include(router.urls))
]