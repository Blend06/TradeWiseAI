from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.user_view import UserViewSet

from api.views.chatmessage_view import ChatMessageViewSet
from api.views.cryptoasset_view import CryptoassetViewSet
from api.views.newsarticle_view import NewsarticleViewSet
from api.views.userfeedback_view import UserfeedbackViewSet
from api.views.watchlist_view import WatchlistViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.csrf import csrf_exempt
from api.views.controlpanel_view import ControlPanelView
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'chatmessage', ChatMessageViewSet)
router.register(r'cryptoasset', CryptoassetViewSet)
router.register(r'newsarticle', NewsarticleViewSet)
router.register(r'userfeedback', UserfeedbackViewSet)
router.register(r'watchlist', WatchlistViewSet)

urlpatterns = [
     path('', include(router.urls)),

     path('control-panel-data/', ControlPanelView.as_view(), name='control-panel-data'),
     path('token/',          csrf_exempt(TokenObtainPairView.as_view()), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(),    name='token_refresh'),

   
]