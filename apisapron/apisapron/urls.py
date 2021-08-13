from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path, re_path
from django.urls.conf import include
from django.contrib import admin
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.routes')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    re_path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(
        cache_timeout=0), name='schema-json')

]
