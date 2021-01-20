from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path("api/user/", include("apps.user.urls", namespace="user")),
    path("api/post/", include("apps.post.urls", namespace="post")),
]

if settings.DEBUG:
    from django.urls import re_path
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    urlpatterns += [
        path("admin/silk/", include("silk.urls", namespace="silk_urls")),
    ]
    schema_view = get_schema_view(
        openapi.Info(
            title="tradecore_test API",
            default_version='v1',
            description="tradecore_test API Documentation",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        path('api/docs', schema_view.with_ui('swagger', cache_timeout=0),
             name='schema-swagger-ui'),
        re_path(r'api/docs(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0),
                name='schema-json'),
        path('api/redoc', schema_view.with_ui('redoc', cache_timeout=0),
             name='schema-redoc'),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
