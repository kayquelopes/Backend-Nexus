from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

from core.views import UserViewSet
from core.views import AutorViewSet
from core.views import GeneroViewSet
from core.views import EditoraViewSet
from core.views import IdiomaViewSet
from core.views import StatusViewSet
from core.views import FrequenciaViewSet
from core.views import ClassificacaoIndicativaViewSet
from core.views import HQViewSet


router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'autores', AutorViewSet, basename='autores')
router.register(r'generos', GeneroViewSet, basename='generos')
router.register(r'editoras', EditoraViewSet, basename='editoras')
router.register(r'idiomas', IdiomaViewSet, basename='idiomas')
router.register(r'estados', StatusViewSet, basename='estados')
router.register(r'frequencias', FrequenciaViewSet, basename='frequencias')
router.register(r'classificacoes', ClassificacaoIndicativaViewSet, basename='classificacoes')
router.register(r'hqs', HQViewSet, basename='hqs')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
