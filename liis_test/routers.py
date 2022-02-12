from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title='Example',
        default_version='v1',
        description='',
        contact=openapi.Contact(url='')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='chema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='chema-redoc'),
    path('api/v1/', include('core.urls')),
]