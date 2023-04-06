from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from .views import UserViewSets
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_extensions.routers import ExtendedSimpleRouter

router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
router.register(r'users', UserViewSets)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
